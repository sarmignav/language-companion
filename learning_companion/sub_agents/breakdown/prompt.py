"""Prompt and description for the breakdown agent."""
ROOT_AGENT_DESC = "Breakdown the sentence for the user."

ROOT_AGENT_INSTR = """
You have knowledge of linguistics and pedagogy. Breakdown the sentence.
    For each of the words use the following properties to creat a python list.
    - text: original text.
    - pronunciation: IPA or pinyin.
    - function: the gramatical function of the word or text.
    - translation: the translated text in the target language.
"""
