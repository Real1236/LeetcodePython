# Imagine that you are given some text that a user would like to send as a sequence of SMS messages. However, there is a limit specifying the maximum number of characters a single message can contain. Your task is to split all characters of text into the minimum number of SMS messages possible.

# Each message must contain a part of the text, followed by the suffix <X/Y>, where Y is the total number of messages and X is the number of the current message (starting from 1). The suffix is considered to be a part of the message, so the total length of each message includes the length of the suffix. Only the last message in the sequence can be shorter than limit characters.

# Iterate over all numbers of messages Y starting from 1. Remember to split text into as few SMS messages as possible. Return an array containing the sequence of SMS messages corresponding to this split. If it's not possible to split the text into different messages based on the limit, return an empty array.

# Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(text.length2) will fit within the execution time limit.

# Example

# For text = "Hello, world!" and limit = 10, the output should be

# solution(text, limit) = ["Hello<1/3>",
#                          ", wor<2/3>",
#                          "ld!<3/3>"]
# Expand to see the example video.

# Note: If you are not able to see the video, use this link to access it.

# Note: In this example, an output of ["Hell<1/3>", "o, w<2/3>", "orld!<3/3>"] is an incorrect solution because the first and second messages don't reach the length of limit characters.

# For text = "Very long message! More than 10 messages needed." and limit = 10, the output should be

# solution(text, limit) = ["Very<1/13>",
#                          " lon<2/13>",
#                          "g me<3/13>",
#                          "ssag<4/13>",
#                          "e! M<5/13>",
#                          "ore <6/13>",
#                          "than<7/13>",
#                          " 10 <8/13>",
#                          "mess<9/13>",
#                          "age<10/13>",
#                          "s n<11/13>",
#                          "eed<12/13>",
#                          "ed.<13/13>"]
# Expand to see the example video.

# Note: If you are not able to see the video, use this link to access it.

# For text = "CodeSignal" and limit = 6, the output should be solution(text, limit) = [].

# If the total number of messages is less than 10, the length of the suffixes <X/Y> is equal to 5 since X and Y both consist of only one digit. Given that limit = 6, this means that only one character of text can be included in each message.
# The length of "CodeSignal" is 10, so the total number of messages is at least 10. Since the suffix <X/Y> reaches the limit of 6 characters if Y is a two-digit number, it is not possible to fit CodeSignal into any sequence of SMS messages with this character limit.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] string text

# The text that the user attempts to send, which needs to be split into SMS messages.

# Guaranteed constraints:
# 1 ≤ text.length ≤ 1500.

# [input] integer limit

# The maximum number of characters that each SMS message can contain.

# Guaranteed constraints:
# 6 ≤ limit ≤ 100.

# [output] array.string

# The resulting SMS messages from splitting the text and appending the suffixes described above, or an empty array if it is not possible to fit any text into the SMS messages due to the character limit.

def solution(text, limit):
    
    return

# Test cases:
text, limit = "Hello, world!", 10
res = ["Hello<1/3>", ", wor<2/3>", "ld!<3/3>"]
assert solution(text, limit) == res

text, limit = "Very long message! More than 10 messages needed.", 10
res = ["Very<1/13>", " lon<2/13>", "g me<3/13>", "ssag<4/13>", "e! M<5/13>", "ore <6/13>", "than<7/13>", " 10 <8/13>", "mess<9/13>", "age<10/13>", "s n<11/13>", "eed<12/13>", "ed.<13/13>"]
assert solution(text, limit) == res

text, limit = "CodeSignal", 6
res = []
assert solution(text, limit) == res