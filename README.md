# The SWIF Implementation

## Introduction

Self-Sovereign Identity \(SSI\) model is an identity model that restores users' control and sovereignty of their digital identities using blockchain technology.
This project is a part of a research work entitled "Weakness identification framework for SSI management systems using recommendations and a knowledge graph," which is currently under a reviewing process of an international journal.
This project is intended to develop a recommender system that can infer SSI-specific weaknesses from existing knowledge of common security weaknesses from the CWE database.
This project assumed that common security weaknesses are SSI-specific if they have language correlations to the SSI functional requirements of the target SSI management system.


The project is implemented as a Python Command-Line Interface \(CLI\) tool that accepts an XML file of SSI functional requirements (queries), which defines functions of the target SSI management system in natural language text.
Then, the tool will produce a list of common security weaknesses from the CWE database that have language correlations \(i.e., high similarity scores\) to the given queries.