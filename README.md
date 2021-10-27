# loinc2hpoAnnotation

The repository contains the annotation data for the LOINC2HPO project.

Laboratory tests  are uniquely identified in electronic healthcare records (EHR) with Laboratory Observation Identifier Names and Codes (LOINC), which is a universal code system that defines various kinds of clinical laboratory tests and other measurements. 
The outcome of a laboratory test can be represented by a term in the [Human Phenotype Ontology (HPO)](https://hpo.jax.org/app/), which is a logically defined vocabulary for describing medically relevant abnormal phenotypes.


LOINC-coded laboratory tests can be grouped broadly into three categories, those with a quantitative outcome (Qn), an ordered categorical outcome (ordinal, or Ord) and an unordered categorical outcome (nominal, or Nom). 

## Quantitative tests

A quantitative test for an analyte has a normal range, and there are three types of mappings depending on the result of the test: L (lower than normal), N (normal), and H (higher than normal). Take, for instance, a test for the concentration of potassium in the blood (LOINC:6298-4). If the result is high, our procedure infers the corresponding HPO term for [Hyperkalemia, HP:0002153](https://hpo.jax.org/app/browse/term/HP:0002153). Analogously, a low result is mapped to [Hypokalemia, HP:0002900](https://hpo.jax.org/app/browse/term/HP:0002900). The HPO is an ontology of abnormal phenotypes, and thus there is no term that specifically represents a normal test result. However, computational analysis can record negated HPO terms, and the normal test result is represented as NOT [Abnormal blood potassium concentration, HP:0011042](https://hpo.jax.org/app/browse/term/HP:0011042).

## Ordinal tests

Ordinal tests can have a series of ordered outcomes. The majority of the ordinal LOINC tests were mapped to two possible outcomes, POS (positive) or NEG (negative). For instance, the result of the test Nitrite in urine by test strip can be positive (present) or negative (absent). If present, then our approach infers the HPO term [Nitrituria, HP:0031812](https://hpo.jax.org/app/browse/term/HP:0031812); if absent, our approach infers NOT [Nitrituria, HP:0031812](https://hpo.jax.org/app/browse/term/HP:0031812).


## Nominal tests

Nominal tests have a series of outcomes that lack a natural ordering. Yet, some nominal result values are considered abnormal. For instance, LOINC 5778-6, color of urine. Currently, nine abnormal results of this test are mapped to the nine child terms of [Abnormal urinary color, HP:0012086](https://hpo.jax.org/app/browse/term/HP:0012086), including [Red urine, HP:0040318](https://hpo.jax.org/app/browse/term/HP:0040318) and [Dark urine, HP:0040319](https://hpo.jax.org/app/browse/term/HP:0040319).

# Annotations

This repository contains the annotation file for the LOINC2HPO resource. It can be used with software such as the
[loinc2hpo](https://github.com/monarch-initiative/loinc2hpo) Java library. We have curated the file using a Desktop Java application called [loinc2hpoMiner](https://github.com/pnrobinson/loinc2hpoMiner); this app is not needed to use the annotations for applications.

The annotations are contained in a file called loinc2hpo-annotations.tsv. The file has the following fields.

| Column     |     Explanation      |
|------------|:--------------------:|
| loincId    |  LOINC ID            |
| loincScale |  Qn, Ord, or Nom     |
| system     | e.g., FHIR           |
| code       | test outcome         |
| hpoTermId  |  e.g.,HP:0031812     |
| isNegated  |  excluded?           |
| createdOn  | biocuration date     |
| createdBy  | biocurator           |
| version    | annotation version   |
| isFinalized| ready for use ?      |
| comment    | (optional)           |


# Note

Note -- we will be adapting this format shortly to remove the ``isFinalized`` field and add a field for additional ontology information.