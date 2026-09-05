# Maltrail Trails

Maltrail Trails is the static detection content for [Maltrail](https://github.com/stamparm/maltrail):
millions of indicators, sorted into three threat classes, each one attributed to the report it was
extracted from. "Trails" below is shorthand for Maltrail Trails.

New content lands here daily. For the current size, see the newest
[release](https://github.com/stamparm/trails/releases) — it reports the number of trails it was
assembled from.

## License

**TL;DR:** Internal defensive use, research, and teaching are free. If Maltrail Trails is systematically ingested or used as an intelligence source in a commercial product, service, MSSP/MDR offering, DNS/security service, or redistributed feed, you need separate written permission or a commercial licence. Independently obtained IOCs may still be checked against and referenced to Maltrail Trails. Attribution or a link back to the repository does not make otherwise restricted commercial use permitted.

Maltrail Trails is free for **internal defensive use** — including use by companies to protect their own systems — and for bona fide **research, education and teaching**. If you want to build current Trails content or Trails-derived intelligence into a product, service, MSSP/MDR offering, OEM integration or redistributed feed, you need separate written permission. Commercial licensing, exceptions, and proportionate terms for smaller or early-stage projects: **sales@sekuripy.hr**.

Nothing already released is taken back: everything published up to and including [`e7d704c8c`](https://github.com/stamparm/trails/commit/e7d704c8c18f31eed28645cccb40fc53705f94be) remains MIT-licensed forever. New content is published under the [Maltrail Trails Community Data License 1.0](LICENSE.md) and becomes additionally available under CC BY 4.0 three years after publication. The licence covers our curated Trails corpus, not independently sourced facts or Maltrail's third-party runtime feeds.

**For the exact terms, definitions and edge cases, read the [full licence](LICENSE.md).**

### Commercial use clarification

If you obtained an IOC independently and only use Maltrail Trails as a reference or corroborating source, that is fine.

If Maltrail Trails itself is ingested, indexed, processed, correlated, or otherwise used as an input to a commercial product or service, the commercial licence terms apply.

Providing attribution or a link back to Maltrail Trails does not change that.

## Why it is not in the main repository

Content lands here tens of times a day; the engine does not. When the two shared a repository,
`trails/static` accounted for **98.7% of every blob byte in the history** and 9,169 of 9,549
commits, which made `git log`, `git blame` and `git bisect` useless on the code — and meant updating
detection required pulling a new version of the software.

The main repository's history was not rewritten to hide that; the content simply moved here and
stopped growing there.

## How a deployment gets this

Not by cloning. Four times a day a workflow assembles every file into one CSV, compresses it and
publishes it as a release, so a deployment fetches one file:

```text
STATIC_TRAILS_URL https://github.com/stamparm/trails/releases/latest/download/trails.csv.gz
```

That is the default in `maltrail.conf`. Point it at a specific `content-YYYYMMDD-HHMM` release
instead to **pin** a version, so a bad publish is not immediately global.

Each release carries:

| asset | |
| --- | --- |
| `trails.csv.gz` | the assembled set, gzipped |
| `trails.csv.sha256` | sha256 of the **uncompressed** CSV — it identifies the trail set, not one compression of it |

The client checks that 65-byte digest before downloading anything, so a deployment that updates more
often than the content changes transfers 65 bytes. Assets are attested with GitHub's keyless
provenance:

```bash
gh attestation verify trails.csv.gz --repo stamparm/trails
```

Assembly is done by `core/assemble.py` **in the engine repository**, not here. It has to agree with
the engine on normalisation — `VALID_DNS_NAME_REGEX`, `IGNORE_DNS_QUERY_SUFFIXES`, the whitelist,
idna encoding — and a copy living here would drift from it. One implementation, versioned with the
code that must match it.

## File format

A trail file is plain text. One indicator per line, blank lines and `#` comments ignored:

```text
# Aliases: crysan, 3losh, 3loshrat, sheetrat

# Reference: https://twitter.com/CERT_Polska/status/1072793091856392192
# Reference: https://www.cert.pl/news/single/trojan-oraz-ransomware-w-kampanii/

213.152.161.99:47390
213.152.161.100:47390
```

An indicator may be a domain, a URL or `host/path`, an IPv4 address, an `IP:port` pair, a CIDR
range, a JA3/JA4 fingerprint, a certificate hash, or a bracketed regular expression.

**`# Reference:` applies to the indicators below it, until the next one.** That is how the
dashboard cites a detection's source, so putting a citation in the wrong place misattributes every
indicator under it. A bare `# Reference:` with no value deliberately ends a group, so what follows
is not attributed to the citation above.

**`# Aliases:`** lists other names for the same family, once per file.

Both headers are exact: one `#`, one space, capitalised name, one colon, one space. The gate rejects
near-misses like `# Referecne:` rather than silently treating them as ordinary comments.

## The directory decides the threat class

The directory name becomes the classification in every event and feeds the severity the dashboard
shows:

| directory | means | example `info` |
| --- | --- | --- |
| `malware/` | confirmed malicious infrastructure | `asyncrat (malware)` |
| `malicious/` | malicious activity, broader than one family | `magentocore (malicious)` |
| `suspicious/` | worth looking at, not a verdict | `dynamic domain (suspicious)` |

The filename becomes the family name, with underscores as spaces: `apt_kimsuky.txt` →
`apt kimsuky (malware)`.

Only these three names carry meaning. Any other directory is class-less — so a new pile does not
invent a new threat class by accident.

## Every commit is gated

`.github/workflows/gate.yml` runs on every push, in seconds:

- **Reachable on the wire** — an entry that idna refuses, that `VALID_DNS_NAME_REGEX` rejects, or
  whose last label is dropped before lookup can never match anything. It is not detection, it is
  the appearance of detection.
- **No canary matches** — no trail may match a name that must never be flagged. This is the check
  that sees regex trails; a popularity-list intersection cannot, because a pattern is never *equal*
  to a domain.
- **It assembles** — the same code the publisher runs.

A trail here becomes an alert on somebody else's network at three in the morning. `com.cn` was
listed as malware once; it is a ccTLD.

## Contributing

Open a pull request. An indicator needs:

1. **A verifiable source** under a `# Reference:` header — a report, a sandbox run, a VirusTotal
   link. "I saw it" is not a source.
2. **The right directory.** If you are unsure whether something is malicious or merely suspicious,
   it is suspicious.
3. **Specificity.** A shared platform's apex (`azurewebsites.net`), a public suffix, or a CDN edge
   address flags every tenant on it.
4. **The right file** — an existing family file if one fits, rather than a new one.

The gate will tell you if an entry can never match or hits a canary. It cannot tell you whether the
indicator is *correct*; that is what the reference is for.

By submitting material for inclusion in Maltrail Trails, you agree to [§10](LICENSE.md). If your
contribution is accepted or incorporated into the official repository, then to the maximum extent
permitted by law you assign to Mikhail Kasimov and Miroslav Stampar all transferable rights you own
or control in that accepted contribution. Where a right cannot legally be assigned, §10 provides a
perpetual, irrevocable, transferable and sublicensable fallback licence so the accepted contribution
can be maintained, commercially licensed and later made available under CC BY 4.0 with the rest of
Maltrail Trails. A submission that is not accepted or incorporated is not assigned merely because
you sent it. If you do not agree to those terms, do not submit material for inclusion.

5. **False positives** and **false negatives** in trail data — please open an ordinary [issue](https://github.com/stamparm/trails/issues)
or [pull request](https://github.com/stamparm/trails/pulls).

### Derived blacklist

A domain-only list derived from the `malware/` static trails is published at
[`maltrail-malware-domains.txt`](https://github.com/stamparm/trails/releases/latest/download/maltrail-malware-domains.txt).

It can be used as an input to DNS filtering systems, subject to the terms in [`LICENSE.md`](https://github.com/stamparm/trails/blob/main/LICENSE.md). Operators should review and test it before enabling blocking, as threat-intelligence lists can contain false positives or indicators that are not appropriate for every environment.
