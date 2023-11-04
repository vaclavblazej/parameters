//! Given the processed data generate markdown pages.

use std::collections::{LinkedList, HashMap};
use std::fmt;
use std::fs::File;
use std::io::Write;

use regex::Regex;

use crate::data::{Linkable, Data, Set, Source, SourceKey};
use crate::raw::{RawSet, RawSource};

type Result<T> = std::result::Result<T, MarkdownError>;

#[derive(Debug)]
pub enum MarkdownError {
    IdNotFound(String),
    MissingId,
    EmptyKey,
    ErrSubstitutingId(String),
    ErrSubstituting,
}

impl fmt::Display for MarkdownError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            MarkdownError::IdNotFound(key) => write!(f, "id [[{}]] not found", key),
            MarkdownError::MissingId => write!(f, "id is missing"),
            MarkdownError::EmptyKey => write!(f, "error key is empty"),
            MarkdownError::ErrSubstitutingId(key) => write!(f, "error substituting [[{}]]", key),
            MarkdownError::ErrSubstituting => write!(f, "error substituting"),
        }
    }
}

impl Linkable for RawSet {
    fn get_url(&self) -> String {
        self.id.clone()
    }
    fn get_name(&self) -> String {
        self.name.clone()
    }
}

impl Linkable for RawSource {
    fn get_url(&self) -> String {
        match &self.rawsourcekey {
            crate::raw::RawSourceKey::Bibtex { key: _ } => self.id.clone(),
            crate::raw::RawSourceKey::Online { url } => url.clone(),
            crate::raw::RawSourceKey::Unknown => "#".into(),
        }
    }
    fn get_name(&self) -> String {
        match &self.rawsourcekey {
            crate::raw::RawSourceKey::Bibtex { key } => key.clone(),
            crate::raw::RawSourceKey::Online { url } => url.clone(),
            crate::raw::RawSourceKey::Unknown => "unknown".into(),
        }
    }
}

pub trait GeneratedPage {
    fn get_page(&self, builder: &Markdown) -> String;
}

impl GeneratedPage for Set {
    fn get_page(&self, builder: &Markdown) -> String {
        let mut res = String::new();
        res += "## Description\n\n[[handcrafted]]\n\n";
        res += "## Relations\n\n";
        res += "## Timeline\n\n";
        for source in &self.timeline {
            res += &format!("{}\n\n", builder.linkto(&source.raw));
            for showed in &source.showed {
                res += &format!("{}\n\n", showed.text);
            }
        }
        // todo
        // if !set.notes.is_empty() {
        // for note in &set.notes {
        // content += &format_note(note);
        // }
        // }
        // content += &embed_pdf(&format!("../local_{}", set.id), 480);
        // content += &embed_pdf(&format!("../{}", set.id), 480);
        res
    }
}

impl GeneratedPage for Source {
    fn get_page(&self, builder: &Markdown) -> String {
        "generated source page".into()
    }
}

#[derive(Clone, Debug)]
pub struct Address {
    pub name: String,
    pub url: String,
}
impl Linkable for Address {
    fn get_url(&self) -> String { self.url.clone() }
    fn get_name(&self) -> String { self.name.clone() }
}

pub struct Markdown<'a> {
    data: &'a Data,
}

#[derive(Clone, Debug)]
pub enum Mappable {
    Address(Address),
    String(String),
}

impl<'a> Markdown<'a> {

    pub fn new(data: &'a Data) -> Markdown<'a> {
        Markdown { data }
    }

    pub fn substitute_custom_markdown(&self, line: &String, map: &HashMap<&str, Mappable>) -> String {
        let pattern = Regex::new(r"\[\[(?P<capturegroup>[^\]]+)\]\]").unwrap();
        let result = pattern.replace_all(line, |caps: &regex::Captures| {
            let part = caps.name("capturegroup");
            match part {
                Some(raw_name) => {
                    let key = raw_name.as_str();
                    // println!("  substituting [[{}]]", key);
                    match self.process_key(&key.into(), map) {
                        Ok(res) => res,
                        Err(error) => {
                            println!("  {}", error.to_string());
                            "<< substitution error >>".into()
                        }
                    }
                },
                None => {
                    println!("  error substituting");
                    "<< substitution error >>".into()
                },
            }
        });
        result.into()
    }

    pub fn link_id(&self, keys: &mut LinkedList<&str>) -> Result<String> {
        let some_id = keys.pop_front();
        if let Some(id) = some_id {
            if let Some(link) = self.data.links.get(id) {
                Ok(format!("[{}]({})", link.get_name(), link.get_url()))
            } else {
                Err(MarkdownError::ErrSubstitutingId(id.into()))
            }
        } else {
            Err(MarkdownError::ErrSubstituting)
        }
    }

    pub fn process_list_key(&self, keys: &mut LinkedList<&str>) -> Result<String> {
        let mut content = String::new();
        if let Some(key) = keys.pop_front() {
            match key {
                "parameters" => {
                    for parameter in &self.data.parameters {
                        content += &format!("* {}\n", self.linkto(&parameter.raw));
                    }
                }
                "graphs" => {
                    for graph_class in &self.data.graph_classes {
                        content += &format!("* {}\n", self.linkto(&graph_class.raw));
                    }
                },
                "sources" => {
                    for source in &self.data.sources {
                        if let SourceKey::Bibtex { key, formatted_citation } = &source.sourcekey {
                            content += &format!("* {}\n", self.linkto(&source.raw));
                        }
                    }
                },
                unknown => {
                    return Err(MarkdownError::IdNotFound(unknown.into()));
                },
            }
            Ok(content)
        } else {
            Err(MarkdownError::MissingId)
        }
    }

    pub fn process_key(&self, input: &String, map: &HashMap<&str, Mappable>) -> Result<String> {
        let mut words: LinkedList<&str> = LinkedList::new();
        for word in input.split(' ') {
            words.push_back(word);
        }
        if let Some(first_word) = words.pop_front() {
            match first_word {
                "list" => self.process_list_key(&mut words),
                "pdf" => self.embed_pdf(&mut words),
                unknown => {
                    if let Some(res) = map.get(unknown) {
                        match res {
                            Mappable::String(str) => Ok(str.clone()),
                            Mappable::Address(address) => Ok(self.linkto(address)),
                        }
                    } else {
                        words.push_front(unknown);
                        self.link_id(&mut words)
                    }
                },
            }
        } else {
            Err(MarkdownError::EmptyKey)
        }
    }

    pub fn linkto(&self, linkable: &dyn Linkable) -> String {
        format!("[{}]({})", linkable.get_name(), linkable.get_url())
    }

    pub fn embed_pdf(&self, keys: &mut LinkedList<&str>) -> Result<String> {
        let name: String = keys.pop_front().unwrap().into();
        let default = 480;
        let height: u32 = keys.pop_front().and_then(|x| x.parse::<u32>().ok()).unwrap_or(default);
        Ok(format!(
            "\n<object data=\"{}.pdf\" type=\"application/pdf\" width=\"100%\" height=\"{}px\">\
            <embed src=\"{}.pdf\">\
            <p>This browser does not support PDFs. Please download the PDF to view it: <a href=\"{}.pdf\">Download PDF</a>.</p>\
            </embed>\
            </object>\n\n",
            name, height, name, name
            ))
    }

    pub fn format_set(&self, set: &RawSet) -> String {
        let mut content = String::new();
        content += &format!("## {}", set.name);
        content += "\n";
        // todo
        // if !set.notes.is_empty() {
        // for note in &set.notes {
        // content += &format_note(note);
        // }
        // }
        // content += &embed_pdf(&format!("../local_{}", set.id), 480);
        // content += &embed_pdf(&format!("../{}", set.id), 480);
        content
    }

    pub fn make_page(&self, pagename: &str, content: String) {
        let mut final_markdown = String::new();
        final_markdown += "---\n";
        final_markdown += "layout: \"single\"\n";
        final_markdown += "title: \"Hierarchy of Parameters\"\n";
        final_markdown += "---\n";
        final_markdown += "<!--this is a generated file-->\n\n";
        final_markdown += &content;
        let filename = format!("./build/{}", pagename);
        let mut file = File::create(&filename).expect("Unable to create file");
        file.write_all(final_markdown.as_bytes())
            .expect("Unable to write data to file");
        // println!("Saved website into {}", filename);
        // builder.make_page("_index.md", builder.landing_page_keys(&data));
        // for entry in &data.parameters {
            // builder.make_page(&format!("{}.md", entry.id), builder.format_set(entry));
        // }
    }

}
