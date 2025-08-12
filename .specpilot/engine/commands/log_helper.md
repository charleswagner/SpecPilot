### ## 📝 Log Helper Command

**Purpose**: Implements the Logging Helper interface for all protocols to ensure consistent, timestamped logging across the SpecPilot framework.

---

## **Core Logging Functions**

### **1. Milestone Logging**
- **Function**: `log_milestone(event_emoji, event_type, message)`
- **Purpose**: Writes timestamped entries to `specpilot.log`
- **Format**: `YYYY-MM-DD HH:MM:SS - [current_user_id] - {event_emoji} - [{event_type}] - {message}`
- **Location**: `.specpilot/workspace/[current_user_id]/logs/specpilot.log`

### **2. Verbose Logging**
- **Function**: `log_verbose(transcript_data)`
- **Purpose**: Writes transcript batches to `specpilot_verbose.log`
- **Format**: User-specific transcript blocks with fenced sections
- **Location**: `.specpilot/workspace/[current_user_id]/logs/specpilot_verbose.log`

### **3. Directory Management**
- **Function**: `ensure_logs_directory()`
- **Purpose**: Creates user-specific logs directory if missing
- **Behavior**: Logs `[LOG_DIR_CREATED]` if directory is created

### **4. Log Migration**
- **Function**: `migrate_logs_if_needed()`
- **Purpose**: Moves logs from old user workspaces (e.g., `cursor/`) to current user
- **Behavior**: Logs `[LOGS_MIGRATED]` with source and destination

---

## **Usage Instructions**

### **For Protocols (Mode Switches & Events)**
```
📝 - [LOG_HELPER] - log_milestone("🚀", "MODE_SWITCH", "Switched to Pilot Mode")
```

### **For Transcript Batching**
```
📝 - [LOG_HELPER] - log_verbose("USER: Enter Pilot Mode\nCURSOR: [Response content]")
```

### **For Directory Operations**
```
📝 - [LOG_HELPER] - ensure_logs_directory()
📝 - [LOG_HELPER] - migrate_logs_if_needed()
```

---

## **Implementation Requirements**

### **Error Handling**
- **File Write Failures**: Log `⚠️ - [AI_ERROR] - Logging failure at [path]: [error]` to whichever file can be written
- **Permission Issues**: Gracefully handle directory creation failures
- **Migration Failures**: Continue operation if log migration fails

### **Performance Considerations**
- **Immediate Writes**: Milestone logs written immediately for real-time tracking
- **Batched Transcripts**: Verbose logs batched to avoid excessive I/O
- **Directory Checks**: Minimal overhead for directory existence validation

### **Cross-Platform Compatibility**
- **Path Handling**: Use `pathlib.Path` for cross-platform path operations
- **File Permissions**: Handle different permission models across operating systems
- **Encoding**: Use UTF-8 encoding for all log files

---

## **Integration Points**

### **Required in All Protocols**
- **Mode Switches**: Every mode entry must call `log_milestone`
- **Major Events**: All significant operations must be logged
- **Error Conditions**: All errors must be logged with appropriate severity

### **Required in Commands**
- **Command Execution**: Log command start/completion
- **File Operations**: Log file creation, modification, deletion
- **User Interactions**: Log user requests and system responses

---

## **Example Implementation**

When a protocol needs to log a mode switch:

1. **Call the helper**: `📝 - [LOG_HELPER] - log_milestone("🚀", "MODE_SWITCH", "Switched to Pilot Mode")`
2. **Helper executes**: Creates timestamped entry in milestone log
3. **Result**: `2025-01-03 23:45:12 - cwagner - 🚀 - [MODE_SWITCH] - Switched to Pilot Mode`

This ensures consistent, reliable logging across the entire SpecPilot framework. 