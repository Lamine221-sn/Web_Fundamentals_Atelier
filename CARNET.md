# 📒 Mon carnet de bord

**Nom :*Mbengue* 

**Prénom :*Lamine* 

**Adresse de mon site :** https://riider221.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ Sur Github

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Parce que j'ai deployé le site web sur un serveur public via Github

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ google.com

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ Not Found (erreur 404) veut dire que le serveur n’a pas trouvé de page pour ce chemin, car aucune route ne correspond. C’est le serveur qui envoie ce message, pas ton navigateur.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_Flask plante avec une erreur AssertionError.Le site ne démarre plus et l’erreur apparaît dans l’Error log.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie du texte brut : le code HTML avec ses balises tandisque le navigateur interprète ce texte et affiche une page mise en forme, avec des titres, des listes et des images. Tu peux voir le texte envoyé avec Ctrl + U.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ <h1> : titre principal.
<p> : paragraphe de texte.
<ul> : liste à puces.
<li> : un élément de cette liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ L’image s’affiche parce que la balise <img> contient l’adresse (URL) de l’image. Le navigateur envoie une requête à l’autre serveur (Wikimedia) pour la récupérer, puis l’affiche dans ta page. Elle n’a pas besoin d’être sur ton serveur.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Séparer le code Python et le HTML permet à chacun de travailler sur son fichier sans casser celui de l’autre. Le développeur s’occupe de la logique dans flask_app.py, le graphiste de l’apparence dans les templates. Le code est aussi plus lisible et plus facile à modifier.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Les {{ prenom }} sont remplacés par le serveur, avant l’envoi de la page. On le vérifie avec Ctrl + U : le code source reçu par le navigateur contient « Léa » (ou ton prénom), et plus aucun {{ prenom }}.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML décrit la structure de la page (titre, paragraphe, liste, lien). Le CSS décrit son apparence (couleurs, polices, marges).

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Pour /presentation, le navigateur télécharge 2 fichiers : la page HTML (presentation) et la feuille de style (style.css). Avec le logo Python, il y en a un 3ᵉ, et le navigateur essaie aussi de charger favicon.ico. Compte les lignes de ton onglet Réseau pour avoir le nombre exact.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Le navigateur garde les fichiers en cache (copie locale) pour aller plus vite. Il peut donc réafficher l’ancien CSS. Ctrl + F5 force le téléchargement d’une version neuve.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP signifie HyperText Transfer Protocol. Le navigateur envoie la requête, et le serveur envoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ Pour /presentation, il y a en général 3 à 4 requêtes : presentation (le HTML), style.css, l’image (le logo Python ou la BMW) et favicon.ico. Vérifie dans ton onglet Réseau (F12, puis F5) et note le nombre réel que tu vois.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ Le code 200 veut dire « OK, tout va bien ». Le code 404 de la favicon veut dire « introuvable » : ton site n’a pas de petite icône, donc le serveur n’a rien à envoyer.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Les modifications de l’onglet Éléments ne changent que la copie affichée dans ton navigateur. Le serveur n’est pas touché, donc les autres visiteurs reçoivent toujours la page d’origine. Un rechargement les efface aussi chez toi.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Dans https://www.youtube.com/results?search_query=chat, le paramètre s’appelle search_query et sa valeur est chat.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ Le serveur plante parce que int("bonjour") est impossible : « bonjour » n’est pas un nombre, Python lève une ValueError. Pour l’éviter, il faut vérifier la valeur avant de la convertir, avec un try/except ValueError ou .isdigit(). En cas d’erreur, on renvoie un message clair au lieu de planter.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Afficher tel quel ce que l’utilisateur envoie permet d’injecter du HTML ou du JavaScript dans ta page (faille XSS). Un pirate pourrait faire exécuter un script malveillant chez les visiteurs, par exemple pour voler leurs informations. Il faut toujours échapper les données, ce que font automatiquement les templates avec {{ ... }}.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ En GET, les données apparaissent dans l’URL (/salut?prenom=Lamine&ville=Paris). En POST, l’URL reste /salut et les données sont dans le corps de la requête, donc invisibles dans la barre d’adresse

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ Pour une recherche, on choisit GET, parce que l’URL peut être copiée, partagée ou mise en favori. Pour une connexion avec mot de passe, on choisit POST, parce qu’un mot de passe ne doit pas apparaître dans l’URL, qui est gardée dans l’historique et dans les logs.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Non, elles ne sont pas secrètes. Elles sont invisibles dans l’URL, mais on les voit dans l’onglet Réseau (Charge utile), et elles passent en clair si le site n’est pas en HTTPS. Le POST protège de l’affichage dans l’URL, pas de l’espionnage : c’est HTTPS qui chiffre.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ Une erreur 4xx vient du client : mauvaise demande, page inexistante ou accès interdit (404, 403). Une erreur 5xx vient du serveur : bug ou panne (500). Dans le premier cas, le fautif est celui qui demande. Dans le second, c’est le site.

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Le serveur répond par un code 3xx avec un en-tête Location qui donne la nouvelle adresse. C’est ensuite le navigateur qui fait la deuxième requête vers cette adresse, automatiquement

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Exemples : http:// qui redirige vers https://, google.fr qui renvoie vers google.com, ou une page de connexion qui te renvoie vers ton compte une fois identifié.

Observations : sur /home, il y a 2 requêtes : d’abord 302 (avec Location: /), puis 200 sur /. Sur /nimportequoi, le navigateur voit bien un 404. Sans le , 404, le code devient 200, donc Google croirait que la page existe et l’indexerait.

Défi : le code 418 veut dire « I’m a teapot » (je suis une théière). C’est une blague du 1ᵉʳ avril, sans usage réel.
---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ Sans rien remplir, le serveur connaît ton adresse IP, ton navigateur et ton système (User-Agent), et tes langues préférées.

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ Accept-Language permet à Wikipédia d’envoyer la page dans ta langue (français, anglais…) sans que tu la choisisses.

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ Dans l’Access log de PythonAnywhere, cherche une ligne avec 404 : la page demandée est celle du chemin à côté du code. Par exemple /favicon.ico ou /nimportequoi.

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ La « navigation anonyme » n’est pas anonyme pour le serveur : il voit toujours ton IP et tes en-têtes. Elle ne fait que ne pas enregistrer l’historique et les cookies sur ton appareil.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ 

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ 

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ 

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ 
