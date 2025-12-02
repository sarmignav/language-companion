# Language Learning Companion Agent


Language Learning Companion Agent is an AI agent created to help users learn a language.
It can explain text, detect language patterns, breakdown sentences, create vocabulary lists, or easily create lessons from any language content you find online.

## 🔥 What's new

This first version introduces two flows:

- Translate and breakdown a sentence.
- Explain a topic.

I know it doesn't sound like much, but more is coming.

## ✨ Key Features

- Explain phrases and content.
- Breakdown phrases.
- Identify common language patterns.
- Create vocabulary lists.

## 🚀 Installation & Development

The development is done using [Google's Python ADK](https://github.com/google/adk-python), you need to have Python installed, version 3.14+ is recommended.

You can create a container using `containers/Containerfile.adk-python` like this: `podman build -t adk-python -f containers/Containerfile.adk-python .`

- Log into your container, you can use better methods like setting an entry point and workdir but you can also have a totally generic uv image and work from the shell `podman run -it --name adk --rm -v .:/app --network dev -p 8000:8000 adk-python`.
- Then run adk web for an interactive development environment: `adk web --host 0.0.0.0`, host is needed because you are running it inside a container.

## 🤝 Contributing

Contributions are welcome, please open an issue first so we can be sure your merge request will actually be merged.
