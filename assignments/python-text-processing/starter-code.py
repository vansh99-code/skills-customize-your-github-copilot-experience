import os

INPUT_FILE = "sample-text.txt"
OUTPUT_FILE = "summary.txt"


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def count_words(text):
    return len(text.split())


def count_keyword_occurrences(text, keyword):
    return text.lower().split().count(keyword.lower())


def find_sentences_with_keyword(text, keyword):
    sentences = text.split(".")
    return [sentence.strip() for sentence in sentences if keyword.lower() in sentence.lower()]


def transform_sentences(sentences):
    return [sentence.title() for sentence in sentences]


def write_summary(path, summary):
    with open(path, "w", encoding="utf-8") as file:
        file.write(summary)


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Input file not found: {INPUT_FILE}")
        return

    text = read_file(INPUT_FILE)
    word_count = count_words(text)
    keyword = "python"
    keyword_count = count_keyword_occurrences(text, keyword)
    matching_sentences = find_sentences_with_keyword(text, keyword)
    transformed = transform_sentences(matching_sentences)

    print(f"Word count: {word_count}")
    print(f"Keyword '{keyword}' occurrences: {keyword_count}")
    print("Matching sentences:")
    for sentence in transformed:
        print(f"- {sentence}")

    summary = (
        f"Word count: {word_count}\n"
        f"Keyword '{keyword}' occurrences: {keyword_count}\n\n"
        "Transformed sentences:\n"
        + "\n".join(f"- {sentence}" for sentence in transformed)
    )
    write_summary(OUTPUT_FILE, summary)
    print(f"Summary written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
