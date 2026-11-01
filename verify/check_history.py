import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 257:
            obj = json.loads(line)
            for tc in obj.get('tool_calls', []):
                print(tc.get('args', {}).get('Content', '')[:1000])
