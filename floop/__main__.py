import panther_sdk


def run() -> None:
    panther_sdk.detection.Rule(
        rule_id="Example",
        log_types="Example",
        severity=panther_sdk.detection.SeverityCritical,
        filters=[]
    )


if __name__ == "__main__":
    run()
