* [Table_of_Contents](#Table_of_Contents)
* [markdown-toc](#markdown-toc)
  * [The_Features](#The_Features)
    * [The_Features](#The_Features)
      * [The_Features](#The_Features)
    * [The_Features](#The_Features)
* [environmentaldependence](#environmentaldependence)
  * [the_JDK](#the_JDK)
  * [Maven](#Maven)
* [quick_start](#quick_start)
  * [maven_introduced](#maven_introduced)
  * [md_file](#md_file)
  * [quick_start](#quick_start)
* [attribute_configuration](#attribute_configuration)
  * [attribute_description](#attribute_description)
  * [return_value_description](#return_value_description)
* [test_cases](#test_cases)
* [other](#other)

# Table_of_Contents


# markdown-toc

```
  _ __ ___   __ _ _ __| | ____| | _____      ___ __       | |_ ___   ___ 
 | '_ ` _ \ / _` | '__| |/ / _` |/ _ \ \ /\ / / '_ \ _____| __/ _ \ / __|
 | | | | | | (_| | |  |   < (_| | (_) \ V  V /| | | |_____| || (_) | (__ 
 |_| |_| |_|\__,_|_|  |_|\_\__,_|\___/ \_/\_/ |_| |_|      \__\___/ \___|
 
```

[![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.github.houbb/markdown-toc/badge.svg)](http://mvnrepository.com/artifact/com.github.houbb/markdown-toc)
[![Build Status](https://www.travis-ci.org/houbb/markdown-toc.svg?branch=release_1.0.2)](https://www.travis-ci.org/houbb/markdown-toc?branch=release_1.0.2)
[![Coverage Status](https://coveralls.io/repos/github/houbb/markdown-toc/badge.svg?branch=release_1.0.2)](https://coveralls.io/github/houbb/markdown-toc?branch=release_1.0.2)

Markdown-to-toc can be used to generate a directory of the Markdown page for github page rendering.

- README


> note

For the title, there are two kinds of md grammar [setext] (http://docutils.sourceforge.net/mirror/setext.html)
And [atx] (http://www.aaronsw.com/2002/atx/) mode.

**atx** form is only supported temporarily.

## The_Features

- Github Markdown file one click to generate the directory

- fluent and elegant writing is supported

### The_Features

- Github Markdown file one click to generate the directory

- support multiple generation

#### The_Features

- Github Markdown file one click to generate the directory

### The_Features

- Github Markdown file one click to generate the directory

- support the generation of duplicate titles

- supports filtering of special characters

- supports specifying different file codes

- supports batch processing of files in folders (you can specify whether subfolder files are included)

- supports writing to files, returns contents of the directory, and allows users to process by themselves

- support multi-threads for directory files.

- support i18n

- support gen toc number

# environmental dependence

## the_JDK

JDK8+, make sure the JDK is set up correctly.

Note: If you are use jdk7，download this code and compile by yourself.
## Maven

Jars are managed uniformly using [Maven](http://maven.apache.org/).

Change log

> [change log](doc/changelog/CHANGELOG-ENGLISH.MD)

# quick_start

## maven_introduced

```xml
<dependency>
    <groupId>com.github.houbb</groupId>
    <artifactId>markdown-toc</artifactId>
    <version>${maven-version}</version>
</dependency>
```

## md_file

The project for the support of md file name suffix `.md` or `.markdown`

## quick_start

- single file

```Java
AtxMarkdownToc.newInstance().genTocFile(path);
```

Where path is the path of md file

- specified folder

```Java
AtxMarkdownToc.newInstance().genTocFile(path);
```

Where path is the parent class folder of the md file

# attribute_configuration

- code examples

```Java
AtxMarkdownToc.newInstance()
                .charset("UTF-8")
                .write(true)
                .subTree(true);
```

## attribute_description
 
|:----|:----|:----|:----|
| 1 | charset | `UTF-8` | file charset | 
| 2 | write | `true` | will toc written to the file (default write) | 
| 3 | subTree | `true` | does it include subfolders(default includes) | 
| 3 | order | `false` | does it gen toc order num(default false, since 1.0.5) | 


## return_value_description

`genTocFile()` returns TocGen, `genTocDir()` returns List<TocGen>

- TocGen attribute description
 
|:----|:----|:----| :----|
| 1 | filePath | String | current md filePath |
| 2 | tocLines | List<String> | current md file toc content |

# test_cases

[a single file - directory to generate test cases](https://github.com/houbb/markdown-toc/blob/release_1.0.2/src/test/java/com/github/houbb/markdown/toc/core/impl/AtxMarkdownTocFileTest.java)

[folder - directory to generate test cases](https://github.com/houbb/markdown-toc/blob/release_1.0.2/src/test/java/com/github/houbb/markdown/toc/core/impl/AtxMarkdownTocDirTest.java)

# other

> [Issues & Bugs] (https://github.com/houbb/markdown-toc/issues)
