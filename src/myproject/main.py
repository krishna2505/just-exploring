import logging

# ── Setup ──────────────────────────────────────────────
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


# ── Logic ──────────────────────────────────────────────
def validate_record(record):
    if "name" not in record:
        raise KeyError("Missing required field: name")
    if not isinstance(record.get("age"), int):
        raise ValueError(f"Invalid age: {record.get('age')} — expected integer")
    return True


def process_records(records):
    passed = []
    failed = []

    for record in records:
        try:
            validate_record(record)
            logger.info(f"Valid record: {record}")
            passed.append(record)
        except KeyError as e:
            logger.error(f"Missing field — {e} | Record: {record}")
            failed.append(record)
        except ValueError as e:
            logger.error(f"Invalid value — {e} | Record: {record}")
            failed.append(record)

    return passed, failed


def summarise(passed, failed):
    logger.info(f"Processing complete — passed: {len(passed)}, failed: {len(failed)}")


# ── Entry point ────────────────────────────────────────
if __name__ == "__main__":
    records = [
        {"name": "Krishna", "age": 22},
        {"name": "Rahul"},
        {"age": "twenty"},
        {"name": "Priya", "age": 25},
    ]

    logger.info("Starting record processing")
    passed, failed = process_records(records)
    summarise(passed, failed)
    