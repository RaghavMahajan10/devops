# 🧭 Shell Scripting Mastery — Week 1 Notes

## Topic: Foundations of Shell Scripting (Basics + Small Scripts)
**Goal**: Understand shell environment, variables, loops, conditions, and file handling.

## 🧩 1. Introduction to Shell Scripting
### 💡 What is Shell?

A shell is a command-line interface between the user and the Linux kernel.
You can run single commands or group them inside a script file (.sh).

### 🧠 Common Shells:
| Shell | Path | Description |
|-------|------|-------------|
| bash | /bin/bash | Most commonly used shell |
| sh | /bin/sh | Simplest shell (POSIX) |
| zsh | /bin/zsh | More advanced, modern shell |

Check your shell:
```bash
echo $SHELL
```

## 🗃️ 2. Writing and Running a Script
Create a new script file:
```bash
nano myscript.sh
```

Basic Structure:
```bash
#!/bin/bash
# This is a comment
echo "Hello, Raghav!"
```

### Explanation:
- `#!/bin/bash` → Shebang, tells system to use bash interpreter
- `#` → Comment line
- `echo` → Prints text

Run the script:
```bash
bash myscript.sh
# or make it executable
chmod +x myscript.sh
./myscript.sh
```

## ⚙️ 3. Variables
### Syntax:
```bash
name="Raghav"
echo "Hello, $name"
```

### Rules:
- No space around =
- Access variable using $varname
- Use quotes around strings with spaces

### Example:
```bash
#!/bin/bash
greeting="Welcome"
name="Raghav"
echo "$greeting, $name!"
```

Output:
```
Welcome, Raghav!
```

## 🔢 4. Taking User Input
### read Command:
```bash
echo "Enter your name:"
read username
echo "Hello $username!"
```

### Options:
| Option | Description |
|--------|-------------|
| -p | Prompt message inline |
| -s | Silent mode (for passwords) |

### Example:
```bash
read -p "Enter username: " user
read -s -p "Enter password: " pass
```

## 🔁 5. Arithmetic Operations
Using expr (old way):
```bash
expr 5 + 3
```

Using $(( )) (recommended):
```bash
a=10
b=5
echo $((a + b))
echo $((a - b))
echo $((a * b))
echo $((a / b))
```

## ⚖️ 6. Conditional Statements
### Syntax:
```bash
if [ condition ]; then
   commands
elif [ condition ]; then
   commands
else
   commands
fi
```

### Common Conditions:
| Test | Meaning |
|------|---------|
| -e file | File exists |
| -d dir | Directory exists |
| -r file | File is readable |
| -w file | File is writable |
| -x file | File is executable |
| string1 = string2 | Strings equal |
| int1 -eq int2 | Integers equal |
| int1 -gt int2 | Greater than |
| int1 -lt int2 | Less than |

### Example:
```bash
if [ $a -gt $b ]; then
  echo "A is greater"
else
  echo "B is greater"
fi
```

## 🔁 7. Loops in Shell
### for loop
```bash
for i in {1..5}; do
  echo "Number: $i"
done
```

### while loop
```bash
i=1
while [ $i -le 5 ]; do
  echo "Count: $i"
  ((i++))
done
```

### until loop
Runs until condition becomes true.
```bash
i=1
until [ $i -gt 5 ]; do
  echo "Value: $i"
  ((i++))
done
```

## 📄 8. Working with Files and Directories
### Basic Commands:
| Command | Description |
|---------|-------------|
| pwd | Print current directory |
| ls | List files |
| cd <dir> | Change directory |
| mkdir <dir> | Create directory |
| rm <file> | Remove file |
| rmdir <dir> | Remove empty directory |
| cp src dest | Copy file |
| mv src dest | Move/rename file |
| touch file | Create empty file |

### Example:
```bash
mkdir -p ~/projects/scripts
cd ~/projects/scripts
touch test.sh
```

## 🧮 9. File Handling Commands
| Command | Description |
|---------|-------------|
| cat file | Show file content |
| head -n 5 file | Show first 5 lines |
| tail -n 5 file | Show last 5 lines |
| wc file | Count lines, words, chars |
| grep "word" file | Search for pattern |
| sort file | Sort lines alphabetically |
| uniq file | Remove duplicate lines |
| cut -d' ' -f1 file | Extract specific columns |
| find /path -name "*.log" | Find files recursively |

## 🪄 10. Useful Shell Operators
| Operator | Meaning | Example |
|----------|---------|---------|
| && | Run next command only if previous succeeds | mkdir test && cd test |
| ; | Run multiple commands sequentially | echo hi; ls |
| > | Redirect output to file | echo "Hi" > out.txt |
| >> | Append output to file | echo "New line" >> out.txt |
| < | Read input from file | wc < file.txt |
| \| | Pipe output to another command | ls \| grep ".txt" |

## 🧰 11. Error Handling & Debugging
### Exit Codes
Every command returns an exit code (0 = success, nonzero = failure).

Check with:
```bash
echo $?
```

### Debug Mode
Run a script in debug mode to trace commands:
```bash
bash -x myscript.sh
```

## 🧠 12. Memory-Friendly Command Tips
| Goal | Command |
|------|---------|
| Show help for a command | <command> --help |
| Manual page | man <command> |
| Last command | !! |
| View command history | history |
| Repeat specific command | !<line_number> |
| Clear screen | clear or Ctrl + L |
| Auto-complete | Press Tab twice |

## 13. Command-Line Arguments
### 💡 What Are They?

You can pass values to a script when executing it. These values are called positional parameters.

| Variable | Meaning |
|----------|---------|
| $0 | Script name |
| $1 | First argument |
| $2 | Second argument |
| $# | Number of arguments |
| $@ | All arguments |

### 🧠 Example
```bash
#!/bin/bash
echo "Script Name: $0"
echo "First Arg : $1"
echo "Second Arg: $2"
echo "Total Args: $#"
```

Run:
```bash
./args.sh folder1 folder2
```

Output:
```
Script Name: ./args.sh
First Arg : folder1
Second Arg: folder2
Total Args: 2
```

✅ Use command-line arguments to make scripts reusable and dynamic.

## 14. Automatic Backup Script
### 💡 Concept

Automate backup of directories with compression and timestamps.

| Command | Description |
|---------|-------------|
| tar -czf | Create compressed .tar.gz file |
| basename | Extract folder name from path |
| date +%Y%m%d_%H%M | Generate timestamp |
| && | Run next command if previous succeeds |

### 🧩 Script
```bash
#!/bin/bash
src=$1
dest=$2

if [ -z "$src" ] || [ -z "$dest" ]; then
  echo "Usage: ./backup.sh <source> <destination>"
  exit 1
fi

timestamp=$(date +%Y%m%d_%H%M)
file="$dest/$(basename "$src")_$timestamp.tar.gz"

tar -czf "$file" "$src" && echo "Backup created: $file"
```

### 🧾 Run
```bash
./backup.sh /home/raghav/docs /home/raghav/backups
```

✅ Add to cron for daily backups:
```bash
0 2 * * * /path/backup.sh /data /data/backups
```

## 15. Disk Cleanup Automation
### 💡 Concept

Delete files older than N days (e.g., temp/log files) and log deletions.

| Option | Meaning |
|--------|---------|
| -type f | Select only files |
| -mtime +7 | Files older than 7 days |
| -delete | Remove files |
| wc -l | Count lines/items |

### 🧩 Script
```bash
#!/bin/bash
target="/tmp"
log="/var/log/cleanup.log"

count=$(find "$target" -type f -mtime +7 | wc -l)
find "$target" -type f -mtime +7 -delete

echo "$(date): Deleted $count old files from $target" >> "$log"
echo "Cleanup complete. Deleted $count old files."
```

## 16. Log File Analyzer
### 💡 Concept

Analyze system logs and count ERROR, WARNING, INFO entries.

| Command | Description |
|---------|-------------|
| grep -c | Count matching lines |
| grep -i | Case-insensitive search |
| tee | Show and log output |
| (( )) | Arithmetic comparison |

### 🧩 Script
```bash
#!/bin/bash
logfile="/var/log/syslog"

err=$(grep -ci "error" "$logfile")
warn=$(grep -ci "warn" "$logfile")
info=$(grep -ci "info" "$logfile")

echo "Error count  : $err"
echo "Warning count: $warn"
echo "Info count   : $info"

if (( err > 10 )); then
  echo "⚠️  High error rate detected — check logs immediately!"
fi
```

## 17. Website Uptime Monitor
### 💡 Concept

Ping a site multiple times; log downtime if unreachable.

| Command | Purpose |
|---------|---------|
| ping -c 1 | Send 1 ping packet |
| sleep 5 | Wait 5 seconds |
| tee | Print and log together |

### 🧩 Script
```bash
#!/bin/bash
site="google.com"
for i in {1..5}; do
  if ping -c 1 "$site" &>/dev/null; then
    echo "✅ Site reachable."
  else
    echo "❌ Site down (Attempt $i)" | tee -a /var/log/uptime.log
  fi
  sleep 5
done
```

## 18. Core Concepts Recap
| Concept | Example |
|---------|---------|
| Command-line args | $1, $2, $@, $# |
| Compare numbers | (( a > b )) |
| Find old files | find /tmp -mtime +7 |
| Compress backup | tar -czf backup.tar.gz folder |
| Ping check | ping -c 1 google.com |
| Log output | echo "msg" >> logfile |
| Schedule task | crontab -e |

## 19. Functions in Shell
### 💡 What Are Functions?

Functions let you group reusable commands under a name — similar to methods in programming.

**Syntax:**
```bash
function function_name() {
   commands
}
# OR
function_name() {
   commands
}
```

**Example:**
```bash
#!/bin/bash
greet() {
  echo "Welcome, $1!"
}
greet "Raghav"
```
Output:
```
Welcome, Raghav!
```
✅ Functions are great for modular automation scripts (e.g., backup + alert + log in one file).

## 20. Exit Codes and Error Handling
### 💡 Concept

Each command returns an exit code:

| Code | Meaning |
|------|---------|
| 0    | Success |
| 1    | General error |
| 2    | Misuse of shell commands |
| 127  | Command not found |

**Example:**
```bash
#!/bin/bash
mkdir /root/test &>/dev/null
if [ $? -ne 0 ]; then
  echo "❌ Failed to create directory. Permission denied."
else
  echo "✅ Directory created."
fi
```
✅ Use `set -e` to stop script on any error (recommended for automation pipelines).

## 21. Arrays and Loops for Multiple Items
### 💡 Concept

Arrays store multiple values — great for looping through servers, files, or URLs.

**Syntax:**
```bash
arr=("google.com" "yahoo.com" "bing.com")
for site in "${arr[@]}"; do
  echo "Pinging $site"
  ping -c 1 "$site" &>/dev/null && echo "OK" || echo "Down"
done
```
Output:
```
Pinging google.com
OK
Pinging yahoo.com
OK
Pinging bing.com
OK
```
✅ Use this for multi-server health checks or multi-site uptime monitoring.

## 22. Automating Docker Tasks
### 💡 Concept

Shell scripts are commonly used to build, run, and monitor Docker containers automatically.

**Example: Auto Deploy Docker Container**
```bash
#!/bin/bash
image="myapp:latest"
container="myapp_container"

echo "Pulling latest image..."
docker pull $image

if [ "$(docker ps -q -f name=$container)" ]; then
  echo "Stopping old container..."
  docker stop $container && docker rm $container
fi

echo "Starting new container..."
docker run -d --name $container -p 8080:80 $image
echo "✅ Deployment complete."
```
Output:
```
Pulling latest image...
Stopping old container...
Starting new container...
✅ Deployment complete.
```
✅ Useful in CI/CD pipelines for zero-downtime deployments.

## 23. Automated Cloud Backup (AWS CLI Example)
### 💡 Concept

Use AWS CLI with shell scripts to upload local backups automatically.

Pre-requisite: Install & configure AWS CLI
```bash
aws configure
```

**Script:**
```bash
#!/bin/bash
backup_file="/home/raghav/backups/weekly.tar.gz"
bucket="s3://my-zenbyte-backups"

echo "Uploading backup to S3..."
aws s3 cp "$backup_file" "$bucket"

if [ $? -eq 0 ]; then
  echo "✅ Backup uploaded successfully!"
else
  echo "❌ Upload failed. Check AWS CLI credentials."
fi
```
✅ You can use this in conjunction with your Week 2 backup script.

## 24. System Health Monitor (Advanced)
### 💡 Concept

Collect detailed system metrics — CPU, memory, disk, network — and send alerts.

**Example Script:**
```bash
#!/bin/bash
report="/tmp/health_report.txt"

{
echo "===== SERVER HEALTH REPORT ====="
echo "Date: $(date)"
echo "Hostname: $(hostname)"
echo -e "\nCPU Load:"
uptime
echo -e "\nMemory Usage:"
free -h
echo -e "\nDisk Usage:"
df -h
echo -e "\nTop 5 Processes:"
ps aux --sort=-%mem | head -6
} > $report

mail -s "Server Health Report" admin@example.com < $report
```
✅ Send daily health reports via cron:
```bash
0 8 * * * /scripts/system_health.sh
```

## 25. Git & CI/CD Automation
### 💡 Concept

Automate build/test/deploy workflows with Git hooks or CI scripts.

**Example: Auto-Pull Latest Code**
```bash
#!/bin/bash
repo="/var/www/myapp"
cd $repo

echo "Pulling latest code..."
git pull origin main

if [ $? -eq 0 ]; then
  echo "✅ Code updated successfully!"
else
  echo "❌ Git pull failed. Check connection."
fi
```
✅ Combine with your Docker deployment script to auto-update your application on each commit.

## 26. Sending Alerts via Email (Optional)
### 💡 Concept

You can send email alerts directly from shell scripts.

Using mail command:
```bash
echo "Disk space low on $(hostname)" | mail -s "Alert: Disk Usage" admin@example.com
```
Using sendmail:
```bash
sendmail admin@example.com <<EOF
Subject: Alert - High CPU
CPU usage exceeded 90% on $(hostname)
EOF
```
✅ Great for automation alerts, uptime failures, or build notifications.

## 27. Week 3 Core Commands Reference
| Command         | Purpose                |
|-----------------|-----------------------|
| docker ps -a    | List containers       |
| docker stop/start | Manage containers   |
| aws s3 cp       | Upload file to S3     |
| git pull        | Get latest code       |
| uptime, free -h, df -h | Monitor system |
| ps aux          | List processes        |
| mail -s         | Send email            |
| cron            | Schedule jobs         |

## 28. Cron Jobs and Scheduling
### 💡 What Is Cron?

Cron is a scheduler service in Linux that runs tasks at specified intervals.

**Syntax:**
```
* * * * *  command_to_run
| | | | |
| | | | └── Day of week (0–6, Sun–Sat)
| | | └──── Month (1–12)
| | └────── Day of month (1–31)
| └──────── Hour (0–23)
└────────── Minute (0–59)
```

**Examples:**
| Schedule      | Example                   | Meaning                |
|---------------|---------------------------|------------------------|
| 0 0 * * *     | /scripts/backup.sh        | Run daily at midnight  |
| */10 * * * *  | /scripts/check_cpu.sh     | Every 10 minutes       |
| 0 9 * * 1     | /scripts/report.sh        | Every Monday 9 AM      |
| @reboot       | /scripts/startup.sh       | On system startup      |

View/Edit Cron:
```bash
crontab -e
```
List Jobs:
```bash
crontab -l
```

## 29. Real-Time Monitoring with watch and trap
### 💡 Concept

Sometimes you need continuous monitoring — without cron delays.

| Command | Use |
|---------|-----|
| watch   | Run a command repeatedly at intervals |
| trap    | Capture signals like Ctrl+C to cleanly exit |

**Example:**
```bash
#!/bin/bash
trap "echo 'Script stopped safely'; exit" SIGINT

while true; do
  clear
  date
  echo "CPU Load: $(uptime | awk '{print $(NF-2)}')"
  echo "Memory: $(free -m | awk 'NR==2{print $3"/"$2" MB"}')"
  sleep 5
done
```
Output:
```
CPU Load: 0.45
Memory: 1024/4096 MB
```
✅ Use this for continuous health dashboards or live monitoring.

## 30. Remote Server Automation (SSH Loops)
### 💡 Concept

You can execute commands across multiple servers automatically using SSH.

Pre-requisite: Passwordless SSH setup (`ssh-keygen` + `ssh-copy-id user@server`)

**Example:**
```bash
#!/bin/bash
servers=("192.168.1.10" "192.168.1.20" "192.168.1.30")
for host in "${servers[@]}"; do
  echo "Running updates on $host..."
  ssh user@$host "sudo apt update -y && sudo apt upgrade -y"
done
```
✅ Use for multi-server maintenance, package updates, or log collection.

## 31. Real-World DevOps Project — “Auto Deployment Pipeline”
### 🧠 Description

This script automates:
- Pulling latest Git code
- Building Docker image
- Deploying and restarting container
- Sending notification

**Script:**
```bash
#!/bin/bash
repo="/var/www/myapp"
image="myapp:latest"
container="myapp_container"

cd $repo || exit
echo "Pulling latest code..."
git pull origin main

echo "Building Docker image..."
docker build -t $image .

if [ "$(docker ps -q -f name=$container)" ]; then
  echo "Stopping old container..."
  docker stop $container && docker rm $container
fi

echo "Starting new container..."
docker run -d --name $container -p 8080:80 $image

if [ $? -eq 0 ]; then
  echo "✅ Deployment successful"
  echo "Deployment done at $(date)" | mail -s "Deployment Success" devops@zenbyte.com
else
  echo "❌ Deployment failed"
  echo "Deployment failed at $(date)" | mail -s "Deployment Failed" devops@zenbyte.com
fi
```
✅ You’ve now built a mini CI/CD pipeline in pure shell.

## 32. Multi-Server Log Collector
### 💡 Concept

Collect `/var/log/syslog` or custom logs from multiple servers into one local directory.

**Example:**
```bash
#!/bin/bash
servers=("192.168.1.10" "192.168.1.20")
dest="/home/raghav/server_logs"

mkdir -p "$dest"
for s in "${servers[@]}"; do
  scp user@$s:/var/log/syslog "$dest/syslog_$s.log"
done
echo "✅ Logs collected in $dest"
```
✅ Combine with grep/awk to analyze logs from all servers at once.

## 33. Slack/Telegram Integration (Alerts)
### 💡 Concept

Send notifications directly to Slack/Telegram from scripts using webhooks.

**Example (Slack):**
```bash
#!/bin/bash
webhook_url="https://hooks.slack.com/services/XXXX/XXXX/XXXX"
message="Server $(hostname) CPU usage high: $(uptime | awk '{print $(NF-2)}')"

curl -X POST -H 'Content-type: application/json' \
--data "{\"text\":\"$message\"}" $webhook_url
```
✅ Great for real-time DevOps alerts.

## 34. Parsing JSON and APIs
### 💡 Concept

You can fetch and parse API data using tools like curl and jq.

**Example:**
```bash
#!/bin/bash
data=$(curl -s https://api.github.com/repos/torvalds/linux)
echo "Repo Name: $(echo $data | jq -r '.name')"
echo "Stars: $(echo $data | jq -r '.stargazers_count')"
```
Output:
```
Repo Name: linux
Stars: 165000
```
✅ Learn to parse JSON — critical for API monitoring, DevOps, and cloud automation.

## 35. Week 4 Core Commands Reference
| Command         | Purpose                        |
|-----------------|-------------------------------|
| crontab -e      | Schedule recurring jobs        |
| watch           | Continuously monitor commands  |
| trap            | Capture termination signals    |
| ssh, scp        | Run remote commands / copy files |
| docker, git     | Deploy & version control       |
| curl, jq        | API data retrieval and parsing |
| mail, sendmail  | Send notifications            |
| uptime, df, free, ps | Health metrics           |
