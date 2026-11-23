<div align="center">

# Gabriel Andre

**SRE / Platform Engineer · Kubestronaut**

[![Blog](https://img.shields.io/badge/blog-gabrielandre.com.br-21759B?style=flat-square&logo=wordpress&logoColor=white)](https://blog.gabrielandre.com.br/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-gabrielandre02-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabrielandre02/)
[![Credly](https://img.shields.io/badge/Credly-certifications-FF6F00?style=flat-square&logo=credly&logoColor=white)](https://www.credly.com/users/gabriel.andre)

</div>

I run and troubleshoot production platforms: Kubernetes clusters (RKE2, OpenShift, OKE), GitOps pipelines and the monitoring around them. I keep a homelab to test things before they reach production, and I write about what I learn. Day to day: Kubernetes, Argo CD, Istio, Terraform, Ansible, Prometheus and Grafana.

> 🇧🇷 Engenheiro SRE / Plataforma. Trabalho com Kubernetes, GitOps e observabilidade em produção, e compartilho o que aprendo no blog.

## Open source

I contribute to open source projects in the Kubernetes and GitOps ecosystem.

[![merged PRs](https://img.shields.io/github/issues-search?query=author%3AGabrielandre02+type%3Apr+is%3Amerged+repo%3Aargoproj-labs%2Fargocd-agent+repo%3Akubernetes-sigs%2Fheadlamp+repo%3Aredhat-developer%2Fgitops-operator+repo%3Aeottabom%2Fistio-headlamp-plugin&label=merged%20PRs&color=2ea44f&style=flat-square)](https://github.com/pulls?q=is%3Apr+author%3AGabrielandre02+is%3Amerged+repo%3Aargoproj-labs%2Fargocd-agent+repo%3Akubernetes-sigs%2Fheadlamp+repo%3Aredhat-developer%2Fgitops-operator+repo%3Aeottabom%2Fistio-headlamp-plugin) [![open PRs](https://img.shields.io/github/issues-search?query=author%3AGabrielandre02+type%3Apr+is%3Aopen+repo%3Aargoproj-labs%2Fargocd-agent+repo%3Akubernetes-sigs%2Fheadlamp+repo%3Aredhat-developer%2Fgitops-operator+repo%3Aeottabom%2Fistio-headlamp-plugin&label=open%20PRs&color=58A6FF&style=flat-square)](https://github.com/pulls?q=is%3Apr+author%3AGabrielandre02+is%3Aopen+repo%3Aargoproj-labs%2Fargocd-agent+repo%3Akubernetes-sigs%2Fheadlamp+repo%3Aredhat-developer%2Fgitops-operator+repo%3Aeottabom%2Fistio-headlamp-plugin)

<!-- OSS_CONTRIBUTIONS_START -->

#### Merged pull requests

**[Argo CD Agent](https://github.com/argoproj-labs/argocd-agent) (Multi-cluster architecture for Argo CD)**

* [#1230](https://github.com/argoproj-labs/argocd-agent/pull/1230): fix(principal): add the refresh annotation to an application that has no annotations
* [#1227](https://github.com/argoproj-labs/argocd-agent/pull/1227): docs: remove shipped items from the roadmap
* [#1207](https://github.com/argoproj-labs/argocd-agent/pull/1207): test(ctl): add unit coverage for the config commands and the root command
* [#1206](https://github.com/argoproj-labs/argocd-agent/pull/1206): test(tlsutil): add unit coverage for TLS reloading and key helpers
* [#1205](https://github.com/argoproj-labs/argocd-agent/pull/1205): test(application): add unit coverage for the application manager
* [#1204](https://github.com/argoproj-labs/argocd-agent/pull/1204): test(kube): add unit coverage for the kubernetes client helpers
* [#1203](https://github.com/argoproj-labs/argocd-agent/pull/1203): test(appproject): add unit coverage for the appproject manager
* [#1202](https://github.com/argoproj-labs/argocd-agent/pull/1202): test(repository): add unit coverage for the repository manager
* [#1198](https://github.com/argoproj-labs/argocd-agent/pull/1198): test(replication): add unit coverage for the event forwarder
* [#1197](https://github.com/argoproj-labs/argocd-agent/pull/1197): test(event): add unit coverage for event construction and parsing
* [#1196](https://github.com/argoproj-labs/argocd-agent/pull/1196): test(redisproxy): add unit coverage across parsing, config and connection handling
* [#1195](https://github.com/argoproj-labs/argocd-agent/pull/1195): ci: enable Dependabot updates for GitHub Actions
* [#1194](https://github.com/argoproj-labs/argocd-agent/pull/1194): ci: add /assign and /unassign issue self-assignment workflow
* [#1185](https://github.com/argoproj-labs/argocd-agent/pull/1185): feat: warn that namespace-based mapping is deprecated
* [#1183](https://github.com/argoproj-labs/argocd-agent/pull/1183): fix(agent): keep the re-created app when the principal deletes and re-creates it
* [#1177](https://github.com/argoproj-labs/argocd-agent/pull/1177): ci(e2e): pin goreman and use the go.mod toolchain in the e2e job
* [#1176](https://github.com/argoproj-labs/argocd-agent/pull/1176): fix(e2e): wait for agents to connect before running tests
* [#1173](https://github.com/argoproj-labs/argocd-agent/pull/1173): fix: stop leaking redis subscription goroutines in agent and principal

**[Istio Headlamp plugin](https://github.com/eottabom/istio-headlamp-plugin) (Istio service mesh UI for Headlamp)**

* [#17](https://github.com/eottabom/istio-headlamp-plugin/pull/17): dev: one entrypoint for running the plugin in a local Headlamp
* [#16](https://github.com/eottabom/istio-headlamp-plugin/pull/16): ci: measure unit-test coverage and show it in the job summary
* [#2](https://github.com/eottabom/istio-headlamp-plugin/pull/2): fix: find the Istio control plane outside istio-system

**[OpenShift GitOps operator](https://github.com/redhat-developer/gitops-operator) (Argo CD on OpenShift)**

* [#1569](https://github.com/redhat-developer/gitops-operator/pull/1569): test(dex): use an unknown TLS group in the unsupported curves case
* [#1539](https://github.com/redhat-developer/gitops-operator/pull/1539): chore(e2e): Use DeferCleanup instead of AfterEach cleanup in sequential tests
* [#1538](https://github.com/redhat-developer/gitops-operator/pull/1538): chore(e2e): Use DeferCleanup instead of AfterEach cleanup in parallel tests 1-007 to 1-070
* [#1537](https://github.com/redhat-developer/gitops-operator/pull/1537): chore(e2e): Use DeferCleanup for namespace cleanup in sequential tests 1-083 to 1-135
* [#1536](https://github.com/redhat-developer/gitops-operator/pull/1536): chore(e2e): Use DeferCleanup for namespace cleanup in sequential tests 1-019 to 1-071
* [#1535](https://github.com/redhat-developer/gitops-operator/pull/1535): chore(e2e): Use DeferCleanup for namespace cleanup in parallel tests 1-001 to 1-009
* [#1534](https://github.com/redhat-developer/gitops-operator/pull/1534): chore(e2e): Use DeferCleanup for namespace cleanup in parallel tests 1-091 to 1-144
* [#1533](https://github.com/redhat-developer/gitops-operator/pull/1533): chore(e2e): Use DeferCleanup for namespace cleanup in parallel tests 1-061 to 1-089
* [#1532](https://github.com/redhat-developer/gitops-operator/pull/1532): chore(e2e): Use DeferCleanup for namespace cleanup in parallel tests 1-042 to 1-058
* [#1531](https://github.com/redhat-developer/gitops-operator/pull/1531): chore(e2e): Use DeferCleanup for namespace cleanup in parallel tests 1-019 to 1-039
* [#1504](https://github.com/redhat-developer/gitops-operator/pull/1504): chore(e2e): add CreatePerTestNs and print debug output on every failed spec


<!-- OSS_CONTRIBUTIONS_END -->

## Certifications

<!-- CREDLY:START -->
<p align="center">
  <a href="https://www.credly.com/org/the-linux-foundation/badge/kubestronaut"><img src="https://images.credly.com/images/cd6c6449-6814-4613-a2d3-13cf4ac5be4f/image.png" width="90" alt="Kubestronaut" title="Kubestronaut" /></a>
  <a href="https://www.credly.com/org/the-linux-foundation/badge/cks-certified-kubernetes-security-specialist"><img src="https://images.credly.com/images/9945dfcb-1cca-4529-85e6-db1be3782210/kubernetes-security-specialist-logo2.png" width="90" alt="CKS: Certified Kubernetes Security Specialist" title="CKS: Certified Kubernetes Security Specialist" /></a>
  <a href="https://www.credly.com/org/the-linux-foundation/badge/kcsa-kubernetes-and-cloud-native-security-associate"><img src="https://images.credly.com/images/67dd8a95-8876-4051-9cb9-3d97c204f85a/image.png" width="90" alt="KCSA: Kubernetes and Cloud Native Security Associate" title="KCSA: Kubernetes and Cloud Native Security Associate" /></a>
  <a href="https://www.credly.com/org/google-cloud/badge/associate-cloud-engineer-certification"><img src="https://images.credly.com/images/08096465-cbfc-4c3e-93e5-93c5aa61f23e/image.png" width="90" alt="Associate Cloud Engineer Certification" title="Associate Cloud Engineer Certification" /></a>
  <a href="https://www.credly.com/org/the-linux-foundation/badge/kcna-kubernetes-and-cloud-native-associate"><img src="https://images.credly.com/images/f28f1d88-428a-47f6-95b5-7da1dd6c1000/KCNA_badge.png" width="90" alt="KCNA: Kubernetes and Cloud Native Associate" title="KCNA: Kubernetes and Cloud Native Associate" /></a>
  <a href="https://www.credly.com/org/the-linux-foundation/badge/ckad-certified-kubernetes-application-developer"><img src="https://images.credly.com/images/cc8adc83-1dc6-4d57-8e20-22171247e052/blob" width="90" alt="CKAD: Certified Kubernetes Application Developer" title="CKAD: Certified Kubernetes Application Developer" /></a>
  <a href="https://www.credly.com/org/the-linux-foundation/badge/cka-certified-kubernetes-administrator"><img src="https://images.credly.com/images/8b8ed108-e77d-4396-ac59-2504583b9d54/cka_from_cncfsite__281_29.png" width="90" alt="CKA: Certified Kubernetes Administrator" title="CKA: Certified Kubernetes Administrator" /></a>
  <a href="https://www.credly.com/org/red-hat-inc/badge/red-hat-certified-system-administrator-in-openshift"><img src="https://images.credly.com/images/e7a34dc0-feb1-44a1-b8e7-3f825faf1c8e/blob" width="90" alt="Red Hat Certified System Administrator in OpenShift" title="Red Hat Certified System Administrator in OpenShift" /></a>
</p>
<!-- CREDLY:END -->

## Latest from the blog

<!-- BLOG-POST-LIST:START -->- [OCI HomeLab, Part 2: Building Was Only the Beginning](https://blog.gabrielandre.com.br/oci-homelab-part-2-building-was-only-the-beginning/) <sub>18/09/2026</sub>
- [Home Lab on OCI&#39;s Free Tier.](https://blog.gabrielandre.com.br/home-lab-on-ocis-free-tier/) <sub>29/03/2026</sub>
- [GitLab with Traefik: A Hands-On DevOps Lab Using Docker Swarm, Ansible, and Vagrant](https://blog.gabrielandre.com.br/gitlab-with-traefik-a-hands-on-devops-lab-using-docker-swarm-ansible-and-vagrant/) <sub>04/01/2026</sub>
- [Zabbix Lab - Docker Swarm + Traefik &lpar;Reverse Proxy&rpar; with Vagrant + Ansible](https://blog.gabrielandre.com.br/zabbix-lab-docker-swarm-traefik-reverse-proxy-with-vagrant-ansible/) <sub>01/01/2026</sub>
- [How to Reset the Admin Password in Grafana with PostgreSQL](https://blog.gabrielandre.com.br/how-to-reset-the-admin-password-in-grafana-with-postgresql/) <sub>04/03/2025</sub>
<!-- BLOG-POST-LIST:END -->

➡️ [More posts](https://blog.gabrielandre.com.br/)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Gabrielandre02/Gabrielandre02/output/pacman-contribution-graph-dark.svg" />
  <img alt="Pac-Man contribution graph" src="https://raw.githubusercontent.com/Gabrielandre02/Gabrielandre02/output/pacman-contribution-graph.svg" />
</picture>
