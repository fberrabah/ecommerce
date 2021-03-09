# **Rapport du projet  E-COMMERCE**





## 1 -  Création de la base de donnée.



Tout d'abord il a fallu créer une base de données que nous avons nommé **shop.db** ensuite voir fichier main de la ligne 56 à 81 le code permet la convertion des **fichiers csv** à la base de données **shop.db.**

Il y avait un souci avec le fichier **csv** "product_category_name" que nous avons résolue grâce à la variable **fields** qui corrige cette erreur.

Ensuite il y a eu la création de olist.sql avec les tables et l'ajout des information telle que les clés primaires et secondaires. 

/_\  attention nous avons remarqué dans la base de donnée des doublons de clé primaires 



## 2- Utilisation de la base de donnée.

Pour cela nous avons utilisé des requêtes qui permettent l'utilisation de la base de données **shop.db**  et en ressortir les informations que nous recherchions ce qui nous a permis de répondre aux questions suivante.

Afin de pouvoir lancer mes requêtes j'ai  créé une méthode **create_connection(db_file)** sur mon fichier requete.py qui me permet de me connecter dans ma base de données  que j'ai rajouté dans une variable conn en précisant db_file par **shop.db**  qui représente ma base de données.

Par la suite j'ai créé une méthode **add_requete**  avec une boucle for qui permet de recupéré toute les infos demandée dans ma requête et limité la recherche à 5 lignes.

Ensuite j'appel ma méthode **add_requete** avec mes deux valeur demandée qui son **conn** pour la connextion et **q1** qui correspond à la variable question1 avec la requête correspondante.





**Question 1** : Nombre de client total 

| COUNT customer_unique_id |
| ------------------------ |
| 96096                    |

**Question 2**  : Nombre de produit total 

| DISTINCT product id |
| ------------------- |
| 32951               |

**Question 3** :  Nombre de produit par catégorie

| product_category_name     | COUNT (product_id) |
| ------------------------- | ------------------ |
|                           | 610                |
| agro_industria_e_comercio | 74                 |
| alimentos                 | 82                 |
| alimentos_bebidas         | 104                |
| artes                     | 55                 |

LIMIT 5 info

**Question 4 :**  Nombre de commande total 

| COUNT(dinstinct order_id) |      |
| ------------------------- | ---- |
| 99441                     |      |

**Question 5** :  Nombre de commande selon leurs états

| order_status |      | count(ORDER_ID) |
| ------------ | ---- | --------------- |
| APPROVED     |      | 2               |
| CANCELED     |      | 625             |
| CREATED      |      | 5               |
| DELIVERED    |      | 96478           |
| INVOICED     |      | 314             |

Limit 5 info



**Question 6** : Nombre de commande par mois

| orders | month   |
| ------ | ------- |
| 4      | 9-2016  |
| 324    | 10-2016 |
| 1      | 12-2016 |
| 800    | 01-2017 |
| 1780   | 02-2017 |

**Question 7** : Prix moyen d'une commande

154.10



**Question 8** : Score de satifaction moyen

| order_id                         | AVG(review_score) |
| -------------------------------- | ----------------- |
| 00010242fe8c5a6d1ba2dd792cb16214 | 5                 |
| 00018f77f2f0320c557190d7a144bdd3 | 4                 |
| 000229ec398224ef6ca0657da4fc703e | 5                 |
| 00024acbcdf0a6daa1e931b038114c75 | 4                 |
| 00042b26cf59d7ce69dfabb4e55b4fd9 | 4                 |

**Question 9** : Nombre de vendeur

3095



**Question 10** :  Nombre de vendeur par région 

| SELLER_DATE | COUNT(SELLER_ID) |
| ----------- | ---------------- |
| AC          | 1                |
| AM          | 1                |
| BA          | 19               |
| CE          | 13               |
| DF          | 30               |





#### Pour aller plus loin:



**Question 11 **:   Quantité de produit vendue par catégorie 

| product_category_name     | COUNT(order_item_id) |
| ------------------------- | -------------------- |
|                           | 1603                 |
| agro_industria_e_comercio | 212                  |
| alimentos                 | 510                  |
| alimento_bebidas          | 278                  |
| artes                     | 209                  |

**Question 12:**  Nombre de commande par jours

156.85

**Question 13:** Durée moyenne entre la commande et la livraison

12 jours

**Question 14:**  Nombre de commande par ville (ville du vendeur)



| seller_city     | COUNT(order_item_id) |
| --------------- | -------------------- |
| 04482255        | 1                    |
| abadia de goias | 1                    |
| afonson claudio | 6                    |
| aguas claras df | 1                    |
| alambari        | 5                    |

**Question 15:** Prix minimum des commandes

0€

**Question 16:**  Prix maximum des commandes

13664.08€

**Question 17:**  Le temps moyen d'une livraison par mois

| days | month   |
| ---- | ------- |
| 54   | 09-2016 |
| 19   | 10-2016 |
| 4    | 12-2016 |
| 12   | 01-2017 |
| 13   | 02-2017 |

