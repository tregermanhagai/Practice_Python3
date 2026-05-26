
def is_last_char_exist_more_then_once_in_text(text: str) -> bool:
    """
        Return True if last char appear more then once in the text
        
        Args: text to check
        Example: "text" t appear 2 time so the function will return True
    """
    return text.count(text[-1]) > 1




text = "this is a test text for checking the functionz"
print("Is last char appear more then once ? ",is_last_char_exist_more_then_once_in_text(text) )

