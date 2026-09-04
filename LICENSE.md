# Maltrail Trails Community Data License 1.0

Copyright (c) 2026-present Mikhail Kasimov and Miroslav Stampar.

## Plain-language summary

This summary is provided for convenience only. The terms below govern.

Maltrail Trails ("Trails") is free to use to defend systems and networks that you
or your organization operate.

Trails is also free to use for bona fide research, education, and teaching.

You may use ordinary commercial security software to process Trails for your
own internal defense, and a vendor does not need permission merely because its
product provides a general-purpose feature capable of importing user-supplied
indicators.

However, if you build Trails, or Trails-derived intelligence, into a product,
service, managed-security offering, threat-intelligence feed, detection
platform, or other offering provided to third parties, you need separate
written permission from the Licensors, which may be paid.

The same applies if you use Trails to provide MSSP, MDR, managed SOC, managed
SIEM, commercial incident-response, consulting, OEM, hosted detection, or
similar services to third parties.

These restrictions apply to Licensed Material regardless of how it is
obtained or represented: as an individual repository file, a clone, a release
artifact, an assembled dataset, a converted format, a subset, or a derived
representation.

Historical material does not remain restricted forever. Each item of Licensed
Material, and each substantive modification to it, automatically becomes
available under the Creative Commons Attribution 4.0 International License
(CC BY 4.0) three years after its first public publication.

Material previously published under the MIT License remains MIT-licensed
permanently. Nothing is taken back.

This License does not claim ownership of facts merely because they appear in
Trails. It covers only rights the Licensors actually hold in their curation,
selection, arrangement, classification, attribution, compilation, and other
protectable aspects of the Licensed Material.

---

## 1. Definitions

For purposes of this License, **"Maltrail Trails"** means the data project
maintained in the official repository at
<https://github.com/stamparm/trails>. **"Trails"** is the short name for
Maltrail Trails.

### 1.1 "Licensors"

"Licensors" means Mikhail Kasimov and Miroslav Stampar, together with any
successor or legal entity to which they validly assign their rights in Trails.

### 1.2 "Licensed Material"

"Licensed Material" means the data content published under this License in the
official Maltrail Trails repository at
<https://github.com/stamparm/trails>, including, where applicable:

- threat indicators;
- classifications and categorizations;
- malware, campaign, actor, and family associations;
- source and provenance records;
- references;
- annotations;
- curated groupings;
- selection, arrangement, and organization of the data; and
- other data or metadata expressly identified as being licensed under this
  License.

Licensed Material includes that content in every form in which the Licensors
publish it, whether as individual files in the repository tree or as an
assembled, compressed, converted, filtered, subsetted, or otherwise generated
release artifact.

Without limitation, the release assets `trails.csv.gz`, `trails.csv.sha256`,
`trails-provenance.bin.gz`, `trails-provenance.bin.sha256`,
`maltrail-malware-domains.txt`, and `maltrail-malware-domains.txt.sha256`,
together with any successor, renamed, subset, or derived artifact the
Licensors publish from the repository, are Licensed Material to the extent
they contain material otherwise governed by this License.

Obtaining Licensed Material as a release asset, source archive, `git clone`,
through the GitHub API, through a raw file URL, or by any other means does not
change the license applicable to that material. Pre-Existing MIT Material
remains governed by Section 8, and material that has reached its Change Date
is additionally available under Section 9.

Licensed Material does not include:

(a) Pre-Existing MIT Material as defined in Section 8;

(b) third-party material separately identified as being subject to another
license or other terms;

(c) software source code unless that source code expressly states that this
License applies to it;

(d) any third-party threat-intelligence feed, blocklist, or dataset that a
deployment of Maltrail or other software obtains directly from its publisher;
such feeds are not part of the Licensed Material, and nothing in this License
grants or purports to grant any right in them; or

(e) material in the Maltrail software repository at
<https://github.com/stamparm/maltrail>, including the files under its `data/`
directory, except to the extent a particular item is separately identified as
being governed by this License.

### 1.3 "Licensed Rights"

"Licensed Rights" means copyright, neighboring and related rights,
compilation rights, sui generis database rights, and other legally
protectable rights in databases, collections, selection, arrangement,
curation, or content that the Licensors have authority to license.

### 1.4 "Organization"

"Organization" means a legal entity together with entities that directly or
indirectly control, are controlled by, or are under common control with that
entity.

"Control" means ownership or control of more than fifty percent (50%) of the
voting interests of an entity, or equivalent power to direct its management.

### 1.5 "Authorized Processor"

"Authorized Processor" means a third party that processes Licensed Material
solely on behalf of an individual or Organization exercising Internal
Defensive Use, provided that the third party:

(a) acts only on that individual's or Organization's instructions;

(b) uses the Licensed Material only for that individual's or Organization's
Internal Defensive Use;

(c) does not incorporate the Licensed Material into a shared threat-
intelligence corpus, product, service, or offering for other customers; and

(d) does not independently reuse, aggregate, commercialize, redistribute,
or otherwise exploit the Licensed Material.

A hosting provider, cloud provider, or hosted SIEM may qualify as an
Authorized Processor when these conditions are satisfied.

For avoidance of doubt, a third party acting solely as an Authorized
Processor in accordance with this Section does not engage in Service Provider
Use solely by performing that processing.

### 1.6 "Internal Defensive Use"

"Internal Defensive Use" means use of the Licensed Material solely to detect,
prevent, investigate, analyze, mitigate, or respond to threats affecting
systems, networks, applications, devices, accounts, or data that the using
individual or Organization operates or is responsible for protecting for its
own benefit.

Internal Defensive Use includes:

- ingestion into an internal SIEM, EDR, IDS, firewall, DNS security system,
  data lake, or other defensive system;
- generation of internal alerts, detections, blocks, signatures, rules,
  enrichments, or reports;
- internal reformatting, filtering, indexing, aggregation, or transformation;
- internal incident response and threat hunting; and
- processing by an Authorized Processor.

Internal Defensive Use is available without charge to individuals,
commercial organizations, non-profit organizations, academic institutions,
and government organizations alike.

Use to protect, monitor, investigate, or produce security deliverables for
unaffiliated third parties is not Internal Defensive Use.

### 1.7 "Research and Educational Use"

"Research and Educational Use" means bona fide scientific, academic,
technical, journalistic, educational, or security research or teaching that
does not itself constitute Commercial Product Use or Service Provider Use.

Research and Educational Use may be performed by individuals or by persons
working within commercial, academic, government, or non-profit organizations.

It includes:

- analyzing the Licensed Material;
- conducting experiments or measurements;
- developing and evaluating research methods;
- teaching and classroom use;
- sharing the Licensed Material privately among collaborators participating
  in the same research or educational activity; and
- publishing research findings, aggregate statistics, conclusions, and
  reasonable illustrative extracts.

Research and Educational Use does not include publishing or distributing a
copy, substantial extract, systematic reconstruction, or practical substitute
for the Licensed Material itself before its applicable Change Date.

### 1.8 "Derived Material"

"Derived Material" means a rule, signature, ruleset, indicator set, mapping,
score, enrichment record, classification, transformed dataset, model input,
or other output created through systematic extraction, transformation,
translation, filtering, aggregation, or processing of Licensed Material and
that retains, encodes, or substantially reflects Licensed Material.

Derived Material is subject to this License only to the extent its creation,
reproduction, distribution, extraction, reuse, or other exploitation requires
permission under the Licensed Rights.

Derived Material does not include:

(a) transient or non-distributed operational artifacts of Internal Defensive
Use, such as an internal alert, firewall event, DNS event, ticket, or incident
record generated by a match;

(b) aggregate research findings that do not disclose a substantial or
substitutive portion of the Licensed Material;

(c) general knowledge, techniques, ideas, or methods learned through lawful
use of the Licensed Material; or

(d) independently sourced and independently verified facts that happen to
overlap with facts appearing in Trails.

Nothing in this definition expands the Licensed Rights or claims ownership
over facts or other subject matter that is not legally protectable.

### 1.9 "Redistribution"

"Redistribution" means making Licensed Material or Derived Material available
to an unaffiliated third party in a form that reproduces, exposes,
systematically communicates, or substitutes for a material portion of the
Licensed Material.

Redistribution includes, without limitation:

- public or private feed redistribution;
- database exports;
- downloadable bundles;
- API access;
- mirrors;
- repackaged indicator feeds;
- substantially equivalent transformed datasets; and
- operating or promoting a fork or mirror as an independent distribution
  source, except to the extent the mere act of forking is independently
  authorized by the hosting platform's terms.

Redistribution does not include:

(a) processing by an Authorized Processor;

(b) reasonable illustrative excerpts permitted as Research and Educational
Use;

(c) submitting material back to the Trails project for contribution;

(d) maintaining a public repository fork solely for ordinary contribution,
review, backup, or development purposes where the fork is not operated or
promoted as an independent Trails distribution source; or

(e) merely linking or directing users to the official Trails distribution.

Nothing in this License limits rights independently granted by a repository
hosting platform for use of that platform's own fork functionality. Such
platform-granted rights do not grant any additional right to commercially
exploit, redistribute outside the scope of those platform terms, or use the
Licensed Material for Commercial Product Use or Service Provider Use.

### 1.10 "Commercial Product Use"

"Commercial Product Use" means using Licensed Material or Derived Material,
in whole or in part, in connection with functionality provided to an
unaffiliated third party as part of a commercial product, platform, appliance,
application, service, subscription, feed, feature, or other offering.

This includes use where Licensed Material contributes to:

- detection;
- matching;
- alerting;
- blocking;
- scoring;
- reputation;
- classification;
- enrichment;
- attribution;
- reporting;
- threat intelligence;
- rule or signature generation;
- automated response; or
- similar security functionality.

Commercial Product Use applies whether or not:

- Licensed Material is visible to the customer;
- Licensed Material is distributed in its original format;
- the customer receives raw indicators;
- Licensed Material has been converted into rules, signatures, detections,
  indexes, models, or another representation;
- the relevant functionality is separately priced;
- the relevant functionality is bundled with another product;
- the relevant functionality is included in a paid subscription;
- the relevant functionality appears in a free, community, evaluation, or
  trial tier associated with a commercially offered product or service; or
- revenue is charged specifically for Trails-derived functionality.

Using Licensed Material to train, tune, evaluate, generate, or maintain
detection logic, models, rules, or intelligence that forms part of a
third-party commercial offering is also Commercial Product Use.

### 1.11 "Service Provider Use"

"Service Provider Use" means use of Licensed Material or Derived Material to
protect, monitor, investigate, assess, or produce security outputs or
deliverables for one or more unaffiliated third parties as part of a
commercially provided service.

Service Provider Use includes, without limitation:

- MSSP services;
- MDR services;
- managed SOC services;
- managed SIEM services;
- commercial threat hunting;
- commercial incident response;
- security monitoring;
- threat-intelligence services; and
- consulting services in which Licensed Material materially contributes to
  customer-facing analysis or deliverables.

Service Provider Use applies regardless of whether:

- the customer receives Licensed Material directly;
- the provider charges separately for use of Trails;
- fees are charged per customer;
- the service is bundled into a broader retainer or subscription; or
- Trails is used only as an undisclosed backend input.

### 1.12 "Publication Date"

For an item of Licensed Material, "Publication Date" means the date on which
that item was first made publicly available by the Licensors in substantially
the same form in the official Maltrail Trails repository at
<https://github.com/stamparm/trails> or an official release from that
repository.

Moving, renaming, reorganizing, copying, re-tagging, or mechanically
reformatting material does not reset its Publication Date.

A substantive new addition or substantive modification has its own
Publication Date only with respect to the newly added or substantively
modified material.

### 1.13 "Change Date"

"Change Date" means the date exactly three (3) years after the applicable
Publication Date.

---

## 2. Acceptance and Reservation of Rights

By exercising any permission granted under this License, you accept and agree
to its terms.

If you do not accept these terms, this License grants you no permission to
exercise the Licensed Rights.

Except for rights expressly granted by this License, all rights are reserved.

Nothing in this License limits rights that you possess independently of the
Licensors, including rights arising from Pre-Existing MIT Material, material
that has reached its Change Date, independently obtained facts, rights granted
by third parties, or exceptions and limitations provided by applicable law.

---

## 3. Free Grant for Internal Defensive Use

Subject to the conditions of this License, the Licensors grant you a
worldwide, royalty-free, non-exclusive license under the Licensed Rights to:

- access;
- download;
- reproduce;
- store;
- index;
- analyze;
- filter;
- transform;
- create Derived Material from; and
- otherwise process

the Licensed Material as reasonably necessary for Internal Defensive Use.

You may authorize an Authorized Processor to exercise these rights solely on
your behalf and solely for your Internal Defensive Use. The Authorized
Processor receives no independent right to reuse, aggregate, commercialize,
redistribute, or otherwise exploit the Licensed Material.

No fee or separate commercial agreement is required for Internal Defensive
Use, including Internal Defensive Use by a for-profit Organization.

---

## 4. Free Grant for Research and Educational Use

Subject to the conditions of this License, the Licensors grant you a
worldwide, royalty-free, non-exclusive license under the Licensed Rights to
use, reproduce, analyze, and create Derived Material from the Licensed
Material for Research and Educational Use.

You may publish research papers, technical analyses, presentations,
educational materials, aggregate findings, statistics, and reasonable
illustrative excerpts.

Before the applicable Change Date, this grant does not permit publication or
Redistribution of a substantial portion of Licensed Material or any dataset
that functions as a practical substitute for Trails.

---

## 5. Conditions Applicable to Free Uses

When exercising rights under Sections 3 or 4, you must:

(a) retain this License and applicable copyright notices with stored or copied
versions of the Licensed Material;

(b) not intentionally remove or falsify source, provenance, reference, or
attribution information supplied with the Licensed Material, except where
removal is technically necessary for an otherwise permitted internal
transformation;

(c) preserve such provenance information where reasonably practicable in
Derived Material used internally; and

(d) not state or imply that the Licensors or the Trails project endorse,
certify, sponsor, or warrant your organization, research, product, service, or
findings.

Research or educational publications that materially rely on Trails should
identify Trails, the Licensors, and the applicable version or access date in
a reasonable citation or acknowledgment.

This License does not require Trails attribution to be displayed in each
individual internal alert, event, block, ticket, or other operational artifact.

---

## 6. Uses Requiring Separate Permission

The following are outside the permissions granted by Sections 3 and 4 and
require a separate written agreement with the Licensors before the applicable
Change Date:

- Commercial Product Use;
- Service Provider Use;
- Redistribution; and
- any other use requiring the Licensed Rights that is not expressly permitted
  by this License.

This restriction applies regardless of technical form.

Changing file format, translating indicators into detection rules,
normalizing data, extracting indicators, hashing values, compiling the data
into another database, converting the data to proprietary syntax, generating
signatures, or otherwise transforming the Licensed Material does not by
itself convert a restricted use into a permitted use.

In particular, using Licensed Material as an undisclosed backend input to
customer-facing commercial functionality remains Commercial Product Use or
Service Provider Use where the applicable definition is otherwise satisfied.

---

## 7. General-Purpose Interoperability Is Not Productization

A product, platform, or service does not engage in Commercial Product Use
merely because it provides a general-purpose capability capable of importing,
querying, matching, or processing arbitrary user-supplied indicators and an
end user independently chooses to supply Trails.

This exception applies only where the provider does not itself:

- bundle Licensed Material;
- redistribute Licensed Material;
- operate a Trails mirror;
- automatically obtain Trails on behalf of users;
- preconfigure Trails as a built-in intelligence source;
- maintain a Trails-derived feed for users;
- transform Trails into vendor-maintained detections or intelligence; or
- otherwise use Trails as a vendor-supplied component of the offering.

Nothing prevents a vendor from documenting how users can configure a
general-purpose import mechanism themselves, provided the vendor does not
redistribute the Licensed Material or operate the Trails integration on users'
behalf.

---

## 8. Pre-Existing MIT Material

The following material is "Pre-Existing MIT Material":

All Trails-related material published under the MIT License as part of the
Maltrail repository at <https://github.com/stamparm/maltrail>, or published in
the Maltrail Trails repository at <https://github.com/stamparm/trails> while
that repository stated that it was MIT-licensed, through and including the
following immutable commit in the Maltrail Trails repository:

    MIT BASELINE COMMIT:
    e7d704c8c18f31eed28645cccb40fc53705f94be
    https://github.com/stamparm/trails/commit/e7d704c8c18f31eed28645cccb40fc53705f94be

This includes all material present in the `malware/`, `malicious/`, and
`suspicious/` directories of the Maltrail Trails repository at that revision,
the material under the `trails/` directory of the Maltrail repository from
which it was moved, and any earlier version of that material previously
published under MIT.

Pre-Existing MIT Material remains available under the MIT License
permanently.

Nothing in this License revokes, narrows, terminates, or imposes additional
conditions on rights previously granted under the MIT License.

Where a file contains both Pre-Existing MIT Material and material first added
after the MIT Baseline Commit, the pre-existing portions remain MIT-licensed
and the new portions are governed by the license applicable when those new
portions were first published.

A later substantive modification to Pre-Existing MIT Material may itself be
licensed under this License, but the underlying unmodified MIT-licensed
material remains MIT-licensed.

---

## 9. Delayed Open Licensing

### 9.1 Automatic CC BY 4.0 grant

On its Change Date, the applicable Licensed Material is automatically and
irrevocably offered by the Licensors under the Creative Commons Attribution
4.0 International License (CC BY 4.0), available at
<https://creativecommons.org/licenses/by/4.0/legalcode>, in addition to any
rights previously available under this License.

From the Change Date onward, a recipient may elect to use that material under
CC BY 4.0 instead of this License.

Accordingly, once material reaches its Change Date, commercial use,
redistribution, modification, and other reuse permitted by CC BY 4.0 are
permitted subject to the conditions of CC BY 4.0.

### 9.2 Independent clocks

Each item of Licensed Material, and each substantive modification to it, has
its own Publication Date and Change Date.

The Change Date of one item does not change the license status of newer
material.

### 9.3 No resetting the clock

Moving, renaming, reorganizing, copying, re-tagging, compressing, assembling,
or mechanically reformatting existing Licensed Material does not restart its
three-year period.

Where existing material is substantively modified, only the newly added or
substantively modified portion receives a new Publication Date.

### 9.4 Public repository publication is sufficient

Licensed Material reaches its Change Date three years after its Publication
Date whether or not the Licensors create a formal release containing it.

Failure to create an official release therefore does not indefinitely postpone
the delayed-open conversion.

### 9.5 Scope of the CC grant

The CC BY 4.0 grant applies only to rights the Licensors have authority to
license.

It does not purport to relicense third-party material or extinguish
third-party rights or attribution requirements.

For purposes of CC BY 4.0 attribution, the Licensors request reasonable credit
to:

    Maltrail Trails
    Mikhail Kasimov and Miroslav Stampar
    https://github.com/stamparm/trails
    Licensed under CC BY 4.0

along with an indication of modifications where required by CC BY 4.0.

---

## 10. Contributions and Assignment of Rights

For purposes of this Section, "Contributor" means any person or entity other
than the Licensors that intentionally submits material for inclusion in
Trails after this License takes effect.

By intentionally submitting a contribution to Trails, including through a
pull request, patch, issue attachment, or other contribution mechanism that
identifies this repository or this License, the Contributor agrees to the
following terms as a condition of acceptance of the contribution.

Upon acceptance or incorporation of the contribution into the official
Maltrail Trails repository at <https://github.com/stamparm/trails>, and to the
maximum extent permitted by applicable law, the
Contributor hereby irrevocably assigns, transfers, and conveys to the
Licensors all right, title, and interest the Contributor owns or controls in
the contribution, including all transferable copyright, compilation rights,
database rights, and other intellectual-property rights necessary for the
Licensors to own, use, license, sublicense, relicense, modify, distribute,
commercialize, and otherwise exploit the contribution as part of Trails.

To the extent any such right cannot validly be assigned, transferred, or
conveyed under applicable law, the Contributor instead grants the Licensors a
perpetual, irrevocable, worldwide, royalty-free, transferable, sublicensable
license, with the right to relicense on any terms, to exercise that right in
any manner and for any purpose, including commercial licensing and delayed
publication under CC BY 4.0.

To the maximum extent permitted by applicable law, the Contributor waives,
and agrees not to assert, any moral rights or similar rights that would
prevent or restrict the Licensors from exercising the rights granted or
assigned under this Section.

The Contributor represents and warrants that:

(a) the Contributor has sufficient rights and authority to submit the
contribution on these terms;

(b) the contribution does not knowingly include third-party material that the
Contributor lacks authority to submit on these terms; and

(c) any third-party material intentionally included in the contribution is
clearly identified together with any applicable third-party terms.

The Licensors are not required to accept any contribution.

A contribution that is not accepted or incorporated into the official Trails
repository is not assigned under this Section merely because it was submitted.

No accepted Contributor acquires ownership of Trails, any collective or
compilation copyright in Trails, the Trails name, or any other material merely
by contributing to the project.

Unless the Licensors separately agree in writing, no royalty, fee, accounting,
or other compensation is owed to a Contributor by reason of the Licensors'
use, licensing, sublicensing, relicensing, commercialization, or delayed-open
licensing of an accepted contribution.

---

## 11. Commercial Licenses and Exceptions

The Licensors may grant separate written permission for any use that is
outside this License.

Such permission may be granted:

- commercially;
- without charge;
- as a sponsorship;
- as an OEM agreement;
- under custom attribution requirements; or
- on any other mutually agreed terms.

Nothing in this License requires the Licensors to charge for restricted use,
nor requires them to offer the same terms to every licensee.

Granting an exception or commercial license to one person or organization
does not waive or modify this License for anyone else.

Requests for commercial licensing or other permission should be directed to:

    sales@sekuripy.hr

If that address is ever retired, the current licensing contact is the one
identified in the official Maltrail Trails repository at
<https://github.com/stamparm/trails>.

---

## 12. Facts, Independent Sources, and Rights Not Claimed

Trails contains factual information, including observed domains, IP
addresses, URLs, hashes, infrastructure, malware associations, and other
indicators.

Nothing in this License claims exclusive ownership of a fact merely because
that fact appears in Trails.

In particular, this License does not prevent anyone from independently
discovering, sourcing, observing, verifying, using, or distributing the same
underlying facts.

An indicator independently obtained from another source does not become
subject to this License merely because the same indicator appears in Trails.

Nothing in this License restricts any use that applicable law permits without
permission from the Licensors, including applicable exceptions and
limitations to copyright or database rights.

The restrictions in this License apply only to the extent the Licensors have
Licensed Rights or another legally enforceable basis for imposing the
applicable condition.

---

## 13. Third-Party Material

The Licensed Material may contain references to external reports, research,
feeds, publications, repositories, or other third-party sources.

No right is granted in third-party material beyond the rights that the
Licensors are legally authorized to grant.

A citation, reference, extraction, or inclusion in Trails does not imply that
the Licensors own the underlying third-party report, publication, trademark,
or other external material.

Users remain responsible for complying with any independently applicable
third-party rights.

---

## 14. Termination

Your rights under this License terminate automatically if you materially
breach its terms.

If you cure the violation within thirty (30) days after becoming aware of it,
whether by notice from the Licensors or otherwise, your rights under this
License are automatically reinstated as of the date of cure, unless the
Licensors have separately notified you in writing that the breach is not
eligible for automatic reinstatement because of repeated or intentional
violation.

If a violation is not timely cured, reinstatement requires written permission
from the Licensors.

Termination under this Section affects only rights arising under this
License.

It does not revoke:

- rights validly obtained under the MIT License for Pre-Existing MIT Material;
- rights validly available under CC BY 4.0 after a Change Date; or
- rights granted under a separate agreement, except according to the terms of
  that agreement.

---

## 15. No Trademark Rights or Endorsement

This License does not grant permission to use the names, logos, marks, or
branding of Maltrail Trails, Maltrail, or the Licensors except as reasonably
necessary
for factual attribution.

You may not state or imply sponsorship, certification, approval, partnership,
or endorsement by the Licensors without separate permission.

---

## 16. Disclaimer of Warranty

TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, THE LICENSED MATERIAL IS
PROVIDED "AS IS" AND "AS AVAILABLE", WITHOUT WARRANTY OF ANY KIND, EXPRESS,
IMPLIED, STATUTORY, OR OTHERWISE.

THE LICENSORS DISCLAIM, WITHOUT LIMITATION, WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, TITLE, NON-INFRINGEMENT, ACCURACY,
COMPLETENESS, TIMELINESS, AVAILABILITY, AND FITNESS FOR SECURITY OR DETECTION
PURPOSES.

THE LICENSED MATERIAL MAY CONTAIN ERRORS, OUTDATED INFORMATION, FALSE
POSITIVES, FALSE NEGATIVES, MISCLASSIFICATIONS, INCOMPLETE ATTRIBUTION, OR
OTHER INACCURACIES.

USE OF TRAILS DOES NOT GUARANTEE DETECTION, PREVENTION, IDENTIFICATION, OR
MITIGATION OF ANY SECURITY THREAT.

---

## 17. Limitation of Liability

TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT SHALL THE
LICENSORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
CONSEQUENTIAL, OR OTHER DAMAGES ARISING FROM OR RELATED TO THE LICENSED
MATERIAL OR ITS USE OR INABILITY TO BE USED.

THIS INCLUDES, WITHOUT LIMITATION, LOSS OF DATA, LOSS OF REVENUE, LOSS OF
PROFIT, BUSINESS INTERRUPTION, SECURITY INCIDENTS, MISSED DETECTIONS,
INCORRECT BLOCKING, FALSE POSITIVES, FALSE NEGATIVES, OR DAMAGE RESULTING FROM
RELIANCE ON THE LICENSED MATERIAL.

WHERE APPLICABLE LAW DOES NOT PERMIT A COMPLETE EXCLUSION OF LIABILITY, THE
LIABILITY OF THE LICENSORS SHALL BE LIMITED TO THE MINIMUM AMOUNT PERMITTED BY
APPLICABLE LAW.

---

## 18. License Versions

This document is Maltrail Trails Community Data License 1.0 ("TCDL-1.0").

The Licensors may publish later versions of the Maltrail Trails Community Data
License.

Publishing a later license version does not retroactively remove or narrow
rights already granted for material published under an earlier version.

New Licensed Material may be published under a later license version.

Unless the Licensors expressly state otherwise, a recipient is not entitled
to apply an earlier version of this License to material first published under
a later version.

Material that has reached its Change Date remains available under CC BY 4.0
according to Section 9 regardless of later versions of this License.

---

## 19. Severability and No Waiver

If any provision of this License is held unenforceable in a particular
jurisdiction, that provision shall be interpreted or limited to the minimum
extent necessary to make it enforceable where possible, and the remaining
provisions remain in effect.

Failure by the Licensors to enforce a provision in one instance does not
waive the right to enforce that provision in another instance.

---

## 20. Nature of This License

Before the applicable Change Date, this is a custom data license containing
use restrictions.

It is not an OSI-approved open-source software license, and no representation
is made that it satisfies any particular definition of "open source" or
"open data."

After a Change Date, the applicable historical material is additionally
available under CC BY 4.0 as described in Section 9.

---

END OF MALTRAIL TRAILS COMMUNITY DATA LICENSE 1.0
