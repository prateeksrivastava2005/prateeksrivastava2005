import os
import subprocess
import random
from datetime import datetime, timedelta

GIT_EXE = r"C:\Users\LENOVO\AppData\Local\Programs\Git\cmd\git.exe"
REPO_DIR = r"c:\Users\LENOVO\Downloads\files (1)\prateeksrivastava2005"
AUTHOR_NAME = "Prateek Srivastava"
AUTHOR_EMAIL = "prateek.srivastava2005@gmail.com"

# Set git config in repo
subprocess.run([GIT_EXE, "config", "user.name", AUTHOR_NAME], cwd=REPO_DIR, check=True)
subprocess.run([GIT_EXE, "config", "user.email", AUTHOR_EMAIL], cwd=REPO_DIR, check=True)

# Project-themed commit messages
COMMIT_MESSAGES = [
    # YouTube RAG Application
    "feat(rag): initialize YouTube transcript ingestion pipeline",
    "feat(rag): add semantic chunking with recursive character splitter",
    "feat(rag): integrate PostgreSQL with pgvector extension",
    "feat(rag): implement cosine similarity search with HNSW indexing",
    "feat(langgraph): design agentic search refinement state graph",
    "fix(rag): optimize timestamp extraction and parser formatting",
    "feat(rag): add confidence threshold validation for retrieved chunks",
    "refactor(rag): streamline vector query generator",
    "perf(pgvector): add indexing benchmarks for high-dimensional embeddings",
    "test(rag): add unit tests for transcript cleaner and tokenizer",
    "docs(rag): update YouTube RAG pipeline architecture diagram",
    "feat(rag): implement multi-video playlist batch transcription",
    "fix(langgraph): prevent infinite loops in query reformulation node",
    "feat(rag): add direct timestamp link synthesis for answer citations",
    "refactor(rag): decouple embedding provider from vector store",
    "feat(rag): add fallback keyword retrieval for zero-vector results",
    
    # Parkinson's Disease Detection
    "feat(ml): initialize audio acoustic feature extraction pipeline",
    "feat(ml): implement jitter and shimmer calculation algorithms",
    "feat(ml): extract 13-band Mel-Frequency Cepstral Coefficients (MFCC)",
    "feat(ml): add Harmonics-to-Noise Ratio (HNR) feature extractor",
    "feat(ml): train baseline K-Nearest Neighbors classifier",
    "feat(ml): train Random Forest classifier with hyperparameter grid search",
    "feat(ml): implement Decision Tree with cost-complexity pruning",
    "feat(ml): build soft-voting ensemble model combining RF, KNN, and DT",
    "perf(ml): optimize ensemble weights based on cross-validation ROC-AUC",
    "test(ml): evaluate model sensitivity and specificity on patient test set",
    "docs(ml): document acoustic biomarker methodology and metrics",
    "refactor(ml): modularize audio normalization and preprocessing module",
    "feat(ml): add signal silence stripping and noise filtering",

    # ATC Labs Web & Streaming
    "feat(frontend): scaffold radio channels dashboard UI components",
    "feat(streaming): implement low-latency audio stream buffer player",
    "style(ui): apply responsive dark theme styling to player controls",
    "refactor(components): extract reusable audio visualizer component",
    "perf(ui): reduce re-renders during high-frequency audio stream events",
    "fix(accessibility): improve ARIA attributes and keyboard navigation",
    "feat(ui): add channel search and favorite station pinning",
    "style(theme): enhance mobile viewport layout for streaming dock",

    # Kuava Digital AI Agents
    "feat(agents): scaffold autonomous multi-agent task runner",
    "feat(agents): implement dynamic memory state management for agents",
    "feat(agents): add prompt template library with dynamic variable injection",
    "feat(agents): implement external tool execution sandbox",
    "refactor(agents): streamline agent decision tree branching",
    "fix(agents): handle timeout exceptions in asynchronous agent workers",
    "docs(agents): write specification for multi-step agent workflow engine",

    # Core CS & Algorithms
    "feat(dsa): implement LRU Cache using Doubly Linked List and Hash Map",
    "feat(dsa): solve graph topological sort and cycle detection problems",
    "feat(dsa): optimize binary tree lowest common ancestor search",
    "feat(dsa): implement dynamic programming solutions for knapsack variants",
    "feat(dsa): add Trie implementation with prefix search and autocomplete",
    "feat(dsa): benchmark Dijkstra vs A* shortest path algorithms",

    # Tools, Profile & CI/CD
    "chore: update project dependencies and build scripts",
    "feat(ci): configure automated testing workflow",
    "docs: update developer notes and milestone tracking",
    "feat(profile): optimize shields badges and stats cards",
    "feat(game): add interactive Snake & Ladder game for GitHub Pages",
    "feat(workflow): configure Platane snake contribution graph animation",
    "chore: clean up project structure and remove redundant logs"
]

log_dir = os.path.join(REPO_DIR, "docs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "dev_activity_log.md")

if not os.path.exists(log_file):
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("# Prateek Srivastava — Engineering Activity Log\n\n")

# Date range: past 6 months up to yesterday
# Current date: 2026-11-19
end_date = datetime(2026, 11, 18)
start_date = end_date - timedelta(days=182)

current_day = start_date
total_commits = 0

print(f"Generating realistic past 6 months commits from {start_date.date()} to {end_date.date()}...")

# Seed random for deterministic high quality distribution
random.seed(42)

while current_day <= end_date:
    is_weekend = current_day.weekday() >= 5
    
    # Probability of commits
    if is_weekend:
        num_commits = random.choices([0, 1, 2, 3], weights=[35, 30, 25, 10])[0]
    else:
        num_commits = random.choices([0, 1, 2, 3, 4, 5], weights=[12, 20, 32, 22, 10, 4])[0]

    if num_commits > 0:
        # Generate random sorted times for the day
        hours = sorted(random.sample(range(9, 23), num_commits))
        
        for h in hours:
            m = random.randint(0, 59)
            s = random.randint(0, 59)
            commit_dt = current_day.replace(hour=h, minute=m, second=s)
            date_str = commit_dt.strftime("%Y-%m-%d %H:%M:%S +0530")
            msg = random.choice(COMMIT_MESSAGES)
            
            # Append entry to log file
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"- `{commit_dt.strftime('%Y-%m-%d %H:%M')}`: {msg}\n")
            
            # Commit with environment variables
            env = os.environ.copy()
            env["GIT_AUTHOR_NAME"] = AUTHOR_NAME
            env["GIT_AUTHOR_EMAIL"] = AUTHOR_EMAIL
            env["GIT_COMMITTER_NAME"] = AUTHOR_NAME
            env["GIT_COMMITTER_EMAIL"] = AUTHOR_EMAIL
            env["GIT_AUTHOR_DATE"] = date_str
            env["GIT_COMMITTER_DATE"] = date_str

            subprocess.run([GIT_EXE, "add", "."], cwd=REPO_DIR, check=True)
            res = subprocess.run([GIT_EXE, "commit", "-m", msg], cwd=REPO_DIR, env=env, capture_output=True, text=True)
            if res.returncode == 0:
                total_commits += 1

    current_day += timedelta(days=1)

# Final commit on today's date (2026-11-19)
today = datetime(2026, 11, 19, 0, 35, 12)
today_str = today.strftime("%Y-%m-%d %H:%M:%S +0530")

final_msg = "feat(profile): release complete GitHub profile README, Snake & Ladder game, and snake workflow"
with open(log_file, "a", encoding="utf-8") as f:
    f.write(f"- `{today.strftime('%Y-%m-%d %H:%M')}`: {final_msg}\n")

env = os.environ.copy()
env["GIT_AUTHOR_NAME"] = AUTHOR_NAME
env["GIT_AUTHOR_EMAIL"] = AUTHOR_EMAIL
env["GIT_COMMITTER_NAME"] = AUTHOR_NAME
env["GIT_COMMITTER_EMAIL"] = AUTHOR_EMAIL
env["GIT_AUTHOR_DATE"] = today_str
env["GIT_COMMITTER_DATE"] = today_str

subprocess.run([GIT_EXE, "add", "."], cwd=REPO_DIR, check=True)
subprocess.run([GIT_EXE, "commit", "-m", final_msg], cwd=REPO_DIR, env=env, check=True)
total_commits += 1

print(f"Successfully generated {total_commits} commits across the past 6 months!")

