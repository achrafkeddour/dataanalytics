Pour utiliser le langage R pour l'analyse de données, voici les bases que vous devez connaître :

---

## 1. **Installation de R et RStudio**
- **Installer R :** Téléchargez et installez R depuis le site officiel [CRAN](https://cran.r-project.org/).
- **Installer RStudio :** Un environnement de développement intégré (IDE) populaire pour R, téléchargeable depuis [RStudio](https://posit.co/downloads/).

---

## 2. **Découverte de l'environnement**
- L'environnement RStudio se compose de quatre volets :
  1. Console : Pour exécuter des commandes directement.
  2. Script Editor : Pour écrire et sauvegarder des scripts.
  3. Environment/History : Pour voir les objets créés.
  4. Plots/Packages/Help : Pour les graphiques, la gestion des bibliothèques, et la documentation.

---

## 3. **Manipulation de données de base**
Voici des commandes de base pour commencer à travailler avec des données dans R :

### a. **Créer des objets**
```R
# Vecteurs
vecteur <- c(1, 2, 3, 4, 5)
noms <- c("Alice", "Bob", "Charlie")

# Matrices
matrice <- matrix(1:9, nrow=3, ncol=3)

# Data frames
donnees <- data.frame(
  Nom = c("Alice", "Bob", "Charlie"),
  Age = c(25, 30, 35),
  Score = c(85, 90, 95)
)
```

### b. **Visualiser les données**
```R
# Aperçu des données
head(donnees)  # Les premières lignes
summary(donnees)  # Statistiques descriptives

# Structures des objets
str(donnees)
```

---

## 4. **Importer et exporter des données**
### Importer un fichier CSV
```R
donnees <- read.csv("fichier.csv")
```

### Exporter un fichier CSV
```R
write.csv(donnees, "fichier_sortie.csv", row.names = FALSE)
```

---

## 5. **Analyses statistiques simples**
### Statistiques descriptives
```R
mean(donnees$Score)  # Moyenne
sd(donnees$Score)    # Écart type
```

### Création de graphiques
```R
# Histogramme
hist(donnees$Score, main="Histogramme des scores", xlab="Score")

# Graphique de dispersion
plot(donnees$Age, donnees$Score, main="Âge vs Score", xlab="Âge", ylab="Score")
```

---

## 6. **Utilisation de bibliothèques (packages)**
Les bibliothèques étendent les fonctionnalités de base de R. Voici quelques-unes des plus populaires pour l'analyse de données :
- **ggplot2** : Pour des graphiques complexes.
- **dplyr** : Pour la manipulation de données.
- **tidyr** : Pour le nettoyage de données.

### Installation et chargement des bibliothèques
```R
install.packages("ggplot2")
library(ggplot2)

# Exemple d'utilisation
ggplot(donnees, aes(x=Age, y=Score)) +
  geom_point() +
  labs(title="Relation entre Âge et Score")
```

---

## 7. **Ressources pour aller plus loin**
- **Cours en ligne gratuits :** [Swirl](https://swirlstats.com/) est un package R interactif pour apprendre directement dans RStudio.
- **Documentation officielle :** [CRAN Task Views](https://cran.r-project.org/web/views/).
- **Communauté :** [RStudio Community](https://community.rstudio.com/) ou Stack Overflow.

Vous pouvez maintenant commencer à explorer vos données et créer des visualisations avec R !
