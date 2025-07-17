import json
import hashlib
from collections import defaultdict

def load_data():
    with open("ecfr_data.json") as f:
        return json.load(f)

def word_count_by_agency(data):
    counts = defaultdict(int)
    for part in data.get("parts", []):
        agency = part.get("agency", "Unknown")
        text = part.get("text", "")
        counts[agency] += len(text.split())
    return dict(counts)

def checksum_by_agency(data):
    checksums = defaultdict(list)
    for part in data.get("parts", []):
        agency = part.get("agency", "Unknown")
        text = part.get("text", "")
        checksum = hashlib.md5(text.encode()).hexdigest()
        checksums[agency].append({
            "part": part.get("part_number", "Unknown"),
            "checksum": checksum
        })
    return dict(checksums)

def custom_metric_parts_per_agency(data):
    counts = defaultdict(int)
    for part in data.get("parts", []):
        agency = part.get("agency", "Unknown")
        counts[agency] += 1
    return dict(counts)

def avg_sentence_length_by_agency(data):
    lengths = defaultdict(list)
    for part in data.get("parts", []):
        agency = part.get("agency", "Unknown")
        text = part.get("text", "")
        sentences = text.split('.')
        sentences = [s.strip() for s in sentences if s.strip()]
        word_counts = [len(s.split()) for s in sentences if len(s.split()) > 0]
        if word_counts:
            avg_len = sum(word_counts) / len(word_counts)
            lengths[agency].append(avg_len)
    # Average across all parts per agency
    avg_lengths = {agency: sum(vals) / len(vals) for agency, vals in lengths.items()}
    return avg_lengths

def historical_word_count_by_agency(data):
    # Dummy example of historical counts over years per agency
    # In real app, you'd parse date and aggregate over time
    return {
        "Office of the Federal Register": {"2020": 1200, "2021": 1300, "2022": 1250},
        "Department of Compliance": {"2020": 700, "2021": 800, "2022": 850}
    }

