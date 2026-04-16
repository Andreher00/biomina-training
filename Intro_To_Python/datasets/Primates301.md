# Primate life history and social learning data

Life history data, social learning data, and phylogenetic distance matrix for 301 primate species. These data were assembled and analyzed in Street et al. 2017 (see References).

## Files

- `Primates301.csv` — species-level life history and social learning data
- `Primates301_distance_matrix.csv` — phylogenetic distance matrix

## Variables

### Primates301.csv

| Column | Description |
|--------|-------------|
| `name` | Full taxonomic name of species |
| `genus` | Genus of species |
| `species` | Species name within genus |
| `subspecies` | Sub-species designation, if any |
| `spp_id` | Unique ID for species |
| `genus_id` | Unique ID for genus |
| `social_learning` | Count of mentions of social learning in literature |
| `research_effort` | Size of literature on species |
| `brain` | Brain volume (endocranial volume) in cubic centimeters |
| `body` | Body mass in grams |
| `group_size` | Average social group size |
| `gestation` | Length of gestation (days) |
| `weaning` | Age at weaning (days) |
| `longevity` | Maximum lifespan (months) |
| `sex_maturity` | Age of sexual maturity (days) |
| `maternal_investment` | Period of maternal investment (days) = gestation + weaning |

### Primates301_distance_matrix.csv

Matrix with species on the margins and phylogenetic distances in the cells.
