import argparse
from utils import extract_resources, generate_csp, save_report

def main():
    parser = argparse.ArgumentParser(description="Auto CSP Generator")
    parser.add_argument("url", help="URL of the website")
    args = parser.parse_args()

    resources = extract_resources(args.url)
    csp_policy = generate_csp(resources)
    save_report(args.url, resources, csp_policy)
    print("\nGenerated CSP Policy:\n", csp_policy)

if __name__ == "__main__":
    main()
