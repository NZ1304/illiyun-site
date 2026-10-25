# Illiyun — site vitrine

Site statique de l'application Illiyun (عِلِّيُّون), en trois langues (fr / ar / en),
publié avec GitHub Pages. Aucun outil de build : Python 3 suffit.

## Pages

| Page | Rôle |
|---|---|
| `fr/`, `ar/`, `en/` | Présentation de l'app |
| `*/privacy.html` | Politique de confidentialité (Play Store, loi 09-08) |
| `*/delete-account.html` | Demande de suppression de compte (exigée par Google Play pour les apps avec compte) |
| `*/donate.html` | Soutenir l'app (dons en ligne : à ouvrir) |
| `index.html` | Redirige vers la langue du navigateur (ar, en, sinon fr) |

## Modifier

Tous les textes sont dans `build.py`. Après une modification :

```bash
python build.py
git add -A && git commit -m "..." && git pull --rebase && git push
```

Les pages HTML générées sont commitées (GitHub Pages les sert telles quelles).

## À compléter dans `build.py`

- `CONTROLLER` : responsable du traitement (nom, ville), pour la politique de confidentialité.
- `CNDP_DECLARATION` : numéro de déclaration CNDP, une fois obtenu (sinon la ligne n'apparaît pas).
- `PLAY_URL` : lien Google Play, une fois l'app publiée (remplace « Bientôt sur Google Play »).
- `CONTACT_EMAIL` : adresse de contact, `contact@illiyun.app` depuis le 25 octobre 2026.
- Page Soutenir : lien de don, une fois le moyen de paiement choisi. Attention : Google Play n'accepte les liens de don dans l'app que pour des organismes exonérés d'impôts ; sur le site, pas de restriction.

## Publication et domaine

GitHub Pages : dépôt `illiyun-site` → Settings → Pages → *Deploy from a branch*,
branche `main`, dossier `/ (root)`. Domaine **`illiyun.app`** (acheté le
25 octobre 2026), déclaré par le fichier `CNAME` à la racine (ne pas le supprimer).
L'ancienne adresse `https://nz1304.github.io/illiyun-site/` redirige vers le domaine.

Mise en place (une fois) :

1. Chez le registraire, entrées DNS du domaine :

   | Type | Nom | Valeur |
   |---|---|---|
   | A | `@` | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (4 entrées) |
   | AAAA | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` (4 entrées) |
   | CNAME | `www` | `nz1304.github.io` |

   Garder les entrées MX / TXT de la messagerie (`contact@illiyun.app`).
2. Settings → Pages → Custom domain : `illiyun.app` (déjà rempli par le fichier
   `CNAME`), attendre « DNS check successful ».
3. Cocher **Enforce HTTPS** dès que la case est disponible. Le domaine `.app`
   n'existe qu'en HTTPS (préchargé HSTS dans les navigateurs) : tant que GitHub
   n'a pas émis le certificat (quelques minutes à une heure après le DNS), le
   site n'est pas joignable.
4. Conseillé : GitHub → Settings (du compte) → Pages → *Add a verified domain*
   → `illiyun.app` (entrée TXT), pour que personne d'autre ne puisse le
   rattacher à un dépôt.

Adresses publiques : `https://illiyun.app/` ; confidentialité
`https://illiyun.app/fr/privacy.html` (`en/`, `ar/`) ; suppression de compte
`https://illiyun.app/fr/delete-account.html` (à donner à Google Play).

Plus tard : le même domaine comme adresse d'envoi des codes de connexion
(Brevo / Resend, entrées SPF / DKIM) à la place de Gmail.

## Polices et crédits

Polices hébergées sur le site (aucune requête vers un tiers) : Uthmanic Hafs (Complexe du Roi Fahd),
Noto Naskh Arabic (OFL 1.1), Source Serif 4 (OFL 1.1). L'icône est provisoire, en attendant le logo.
