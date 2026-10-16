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
- `CONTACT_EMAIL` : adresse de contact (aujourd'hui celle qui envoie les codes de connexion).
- Page Soutenir : lien de don, une fois le moyen de paiement choisi. Attention : Google Play n'accepte les liens de don dans l'app que pour des organismes exonérés d'impôts ; sur le site, pas de restriction.

## Publier (une fois)

GitHub → dépôt `illiyun-site` → Settings → Pages → Source : *Deploy from a branch*,
branche `main`, dossier `/ (root)`. Le site est alors à
`https://nz1304.github.io/illiyun-site/`.

## Nom de domaine (plus tard)

1. Acheter le domaine (par ex. `illiyun.app` s'il est libre).
2. Settings → Pages → Custom domain, puis créer chez le registraire les entrées DNS indiquées par GitHub.
3. Cocher « Enforce HTTPS ».
4. Le même domaine servira d'adresse d'envoi des e-mails de connexion (Brevo / Resend) à la place de Gmail.

## Polices et crédits

Polices hébergées sur le site (aucune requête vers un tiers) : Uthmanic Hafs (Complexe du Roi Fahd),
Noto Naskh Arabic (OFL 1.1), Source Serif 4 (OFL 1.1). L'icône est provisoire, en attendant le logo.
