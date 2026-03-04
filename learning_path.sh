#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                  📚 LEARNING PATH - TỔ BỌN CÓ THỂ HỌC                     ║"
echo "║                                                                            ║"
echo "║            Từ Current Level → Production-Ready → Enterprise Scale         ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

cat << 'LEARNING'
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ LEVEL 1: CURRENT (You're Here!) - Time: Ongoing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What you know now:
✅ Docker + Docker Compose
✅ FastAPI + Express.js
✅ JWT authentication
✅ Basic microservices (3-tier)
✅ Telegrambot integration
✅ File-based task queue

Next micro-step:
1. Add Redis caching
   └─ Store frequent queries
   └─ Speed up responses 10x

2. Add PostgreSQL
   └─ Replace file-based inbox
   └─ Use SQL transactions

3. Add Prometheus monitoring
   └─ Track metrics: requests/sec, error rate, latency

Resources:
- https://redis.io/docs/
- https://www.postgresql.org/docs/
- https://prometheus.io/docs/

Time to master: 1-2 weeks each

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 LEVEL 2: STARTUP SCALE - Time: 3-6 months
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Goal: 10x throughput + 99.9% uptime

What you'll learn:
1. KUBERNETES BASICS (2 weeks)
   ├─ Pods, Services, Deployments
   ├─ ReplicaSets (auto-scale)
   ├─ ConfigMaps, Secrets
   └─ Resource limits

   Resources:
   ├─ https://kubernetes.io/docs/
   ├─ https://www.youtube.com/watch?v=X48VuDVv0Z0 (Kubesimplified)
   └─ Practice: Migrate docker-compose to k8s

2. CI/CD PIPELINE (1-2 weeks)
   ├─ GitHub Actions
   ├─ Build + Test + Deploy
   ├─ Automated testing
   └─ Blue-green deployments

   Resources:
   ├─ https://docs.github.com/en/actions
   ├─ https://www.youtube.com/c/TechWithTim (CI/CD)
   └─ Practice: Auto-deploy on every git push

3. OBSERVABILITY (2 weeks)
   ├─ Prometheus (metrics)
   ├─ ELK Stack (logs)
   ├─ Grafana (dashboards)
   └─ Alerting

   Resources:
   ├─ https://prometheus.io/docs/
   ├─ https://www.elastic.co/guide/
   ├─ https://grafana.com/docs/
   └─ Practice: Create alert for high error rate

4. ADVANCED SECURITY (1-2 weeks)
   ├─ OAuth2 instead of JWT
   ├─ TLS/HTTPS everywhere
   ├─ Secrets management (Vault)
   └─ RBAC (Role-based access)

   Resources:
   ├─ https://oauth.net/
   ├─ https://www.vaultproject.io/docs/
   └─ Practice: Add OAuth2 to your system

Result after LEVEL 2:
✅ 10x throughput (600 tasks/hour)
✅ 99.9% uptime SLA
✅ Auto-scaling
✅ Automated deployments
✅ Full observability

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 LEVEL 3: ENTERPRISE SCALE - Time: 6-12 months (after Level 2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Goal: 100x throughput + 99.99% uptime + multi-region

What you'll learn:
1. DISTRIBUTED SYSTEMS (3-4 weeks)
   ├─ Consensus algorithms (Raft)
   ├─ Data replication
   ├─ Fault tolerance
   ├─ Eventual consistency
   └─ Distributed transactions

   Resources:
   ├─ https://raft.github.io/
   ├─ Book: "Designing Data-Intensive Applications"
   ├─ https://newsletter.systemdesign.one/
   └─ Practice: Design a distributed cache

2. MULTI-REGION DEPLOYMENT (2-3 weeks)
   ├─ AWS/GCP multi-region
   ├─ Global load balancing
   ├─ Geo-replication
   ├─ Failover strategies
   └─ DDoS protection

   Resources:
   ├─ https://aws.amazon.com/architecture/
   ├─ https://cloud.google.com/architecture
   └─ Practice: Deploy to 3 regions

3. ADVANCED CACHING (2 weeks)
   ├─ Cache invalidation
   ├─ Redis cluster
   ├─ Cache warming
   └─ Cache prediction (ML)

   Resources:
   ├─ https://redis.io/docs/
   ├─ Book: "The Art of Computer Systems Performance Analysis"
   └─ Practice: Build cache layer

4. MACHINE LEARNING AT SCALE (4 weeks)
   ├─ Model serving (TensorFlow Serving)
   ├─ A/B testing framework
   ├─ Feature stores
   ├─ Model monitoring
   └─ Drift detection

   Resources:
   ├─ https://www.tensorflow.org/serving/
   ├─ https://www.youtube.com/c/StatQuest (Statistics)
   ├─ Book: "Machine Learning Systems Design"
   └─ Practice: Serve ML model at scale

5. ADVANCED SECURITY & COMPLIANCE (4 weeks)
   ├─ Zero-trust security
   ├─ SOC2 compliance
   ├─ HIPAA/GDPR
   ├─ Security scanning (SAST/DAST)
   └─ Incident response

   Resources:
   ├─ https://cheatsheetseries.owasp.org/
   ├─ https://slsa.dev/
   ├─ https://www.sans.org/
   └─ Practice: Pass security audit

Result after LEVEL 3:
✅ 100x throughput (6000+ tasks/hour)
✅ 99.99% uptime SLA
✅ Multi-region active-active
✅ ML models in production
✅ Full compliance (SOC2, HIPAA)
✅ Can compete with startups

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👑 LEVEL 4: GOOGLE-SCALE (Optional mastery) - Time: 12-24 months
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What top companies know:

1. CUSTOM INFRASTRUCTURE
   └─ Build your own Kubernetes
   └─ Custom schedulers
   └─ Custom networking

2. CHAOS ENGINEERING
   └─ Netflix Chaos Monkey
   └─ Gremlin framework
   └─ Test failure scenarios

3. CUSTOM LLM DEPLOYMENT
   └─ Train custom models
   └─ Distributed inference
   └─ Real-time model updates

4. FEDERATED SYSTEMS
   └─ Privacy-preserving ML
   └─ Distributed data
   └─ Decentralized consensus

This is advanced territory - you'll compete with Google!

Resources:
├─ https://www.usenix.org/conference/srecon (Conferences)
├─ https://research.google/ (Google Research Papers)
├─ https://github.com/Netflix (Netflix open-source)
└─ Book: "The Google SRE Book" (free online)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 RECOMMENDED 12-MONTH LEARNING PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MONTH 1-2: Redis + PostgreSQL + Prometheus
└─ Upgrade your current system
└─ Get 5x throughput
└─ Time: 20-30 hours/week

MONTH 3-4: Kubernetes Basics
└─ Understand container orchestration
└─ Migrate docker-compose to k8s
└─ Time: 20-30 hours/week

MONTH 5-6: CI/CD + GitHub Actions
└─ Automate deployment
└─ Add testing pipeline
└─ Time: 15-20 hours/week

MONTH 7-8: Observability Stack
└─ Set up monitoring
└─ Create dashboards
└─ Add alerting
└─ Time: 15-20 hours/week

MONTH 9-10: Advanced Security
└─ OAuth2 implementation
└─ Secrets management
└─ RBAC setup
└─ Time: 15-20 hours/week

MONTH 11-12: Distributed Systems + Multi-region
└─ Design for scale
└─ Multi-region deployment
└─ Disaster recovery
└─ Time: 25-30 hours/week

TOTAL: ~200-250 hours over 12 months = ~4 hours/week

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 BEST RESOURCES TO FOLLOW (Ranked by Quality)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

System Design & Architecture:
1. ⭐⭐⭐⭐⭐ Gaurav Sen - https://www.youtube.com/c/GauravSensei
   └─ Best free system design content

2. ⭐⭐⭐⭐⭐ Martin Fowler - https://martinfowler.com/
   └─ Blogs by industry legend

3. ⭐⭐⭐⭐ High Scalability - http://highscalability.com/
   └─ Real-world architecture analysis

4. ⭐⭐⭐⭐ Newsletter - https://newsletter.systemdesign.one/
   └─ Deep-dive technical articles

Kubernetes & DevOps:
1. ⭐⭐⭐⭐⭐ Official K8s Docs - https://kubernetes.io/docs/
   └─ Best documentation online

2. ⭐⭐⭐⭐ KubeAcademy - https://kube.academy/
   └─ Free courses

3. ⭐⭐⭐⭐ Techworld with Nana - https://www.youtube.com/c/TechWorldwithNana
   └─ K8s + DevOps tutorials

Security:
1. ⭐⭐⭐⭐⭐ OWASP - https://owasp.org/
   └─ Industry standard

2. ⭐⭐⭐⭐ SANS - https://www.sans.org/
   └─ Certifications available

3. ⭐⭐⭐⭐ HackTheBox - https://www.hackthebox.com/
   └─ Hands-on security practice

AI/LLM Integration:
1. ⭐⭐⭐⭐⭐ OpenAI Docs - https://platform.openai.com/docs/
   └─ Best API reference

2. ⭐⭐⭐⭐⭐ Anthropic - https://www.anthropic.com/docs
   └─ Claude API documentation

3. ⭐⭐⭐⭐ LangChain - https://python.langchain.com/
   └─ Framework for LLM apps

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💪 CHALLENGE: Build These Projects to Master Skills
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Project 1: Build a Chat App (Week 1-2)
├─ Requirements: WebSocket, real-time, 100 concurrent users
├─ Stack: Python + FastAPI + WebSocket + PostgreSQL
├─ Learn: Async programming, concurrency
└─ Result: Understand scale limits

Project 2: Build a Job Queue System (Week 3-4)
├─ Requirements: 1000 jobs/sec, retry logic, priority
├─ Stack: Python + Kafka + PostgreSQL
├─ Learn: Message queues, distributed processing
└─ Result: Understand eventual consistency

Project 3: Deploy to Kubernetes (Week 5-6)
├─ Requirements: 3-tier app, auto-scaling, monitoring
├─ Stack: Docker + Kubernetes + Prometheus
├─ Learn: Container orchestration, observability
└─ Result: Understand production operations

Project 4: Multi-region Failover (Week 7-8)
├─ Requirements: Data replication, active-active, < 1sec failover
├─ Stack: AWS + PostgreSQL replication + Route53
├─ Learn: Geo-distribution, disaster recovery
└─ Result: Understand global systems

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You don't need to learn everything at once.

IMMEDIATE (This month):
├─ Add Redis
├─ Add PostgreSQL
├─ Add Prometheus
└─ Time: 2-3 weeks

NEXT 3 MONTHS:
├─ Learn Kubernetes
├─ Set up CI/CD
└─ Time: 1-2 hours/week

NEXT 6-12 MONTHS:
├─ Master observability
├─ Advanced security
├─ Distributed systems
└─ Time: 3-4 hours/week

You're already 70% there. Just keep learning! 🚀

LEARNING
echo ""
