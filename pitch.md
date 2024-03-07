# Pseudocode of duty
# table of content
- [welcome](#welcome)
    - [hellooooo everyone]()
    - [acknowledgment]()
- [team](#team)
    - [who are we?]()
    - [contributions]()
- [fox](#fox)
    - [strategy]()
        - [phase1]()
        - [phase2]()
    - [riddles]()
        - [problem solving]()
            - [easy]()
            - [medium]()
            - [hard]()
        - [security]()
            - [medium](#sec_medium)
            - [hard](#sec_hard)
        - [ML]()
            - [easy]()
            - [medium]()
        - [CV]()
            - [easy]()
            - [medium]()
            - [hard]()
    - [fox challenges]()
        - [new concepts]()

- [eagle]()
    - [what is steganography]()
    - [model]()
    - [data]()
    - [eagle challenges]()    
- [model on bigger scale]()
- [additional use cases]()
- [possible improvements]()

<a id="welcome"></a>

## Welcome
- hello
- acknowledgment 

<a id="team"></a>

## team
- who
- team contributions

<a id="fox"></a>

## fox
### Strategy
### Riddles
#### problem solving
##### easy
- algorithm
    - count frequency --> use map as storing data structure cause o(1) retrieve
    - heapsort --> fast and easy to get max from it

- use cases
    - Natural Language Processing (NLP):
        - Text summarization: Identifying the most frequent words in a document can help in summarizing its content.
        - Sentiment analysis: Analyzing the frequency of certain words can help determine the sentiment of a piece of text.
        - Language modeling: Understanding the distribution of words in a corpus is essential for building accurate language models.

    - Search Engine Optimization (SEO):
        - Keyword analysis: Identifying frequently used keywords in web content helps in optimizing search engine rankings.
        - Content optimization: Analyzing top frequent words in competitors' content can inform content creation strategies.

    - Text Classification:
        - Spam filtering: Analyzing the frequency of certain words in emails or messages can aid in detecting spam.

##### medium
- algorithm
    - uses a stack (monotonic) to decode the string. 
- use cases
    - Image Compression: In image processing, RLE can be used to compress bitmap images. For example, in black and white images where consecutive pixels have the same color, RLE can represent these runs of pixels with a count and the color value, reducing the size of the image data.

    - Text Compression: RLE can be applied to compress text files, especially those containing long sequences of repeated characters or symbols. For example, in DNA sequencing where long sequences of the same nucleotide base are common, RLE can significantly reduce the size of the data.

    - Storage Optimization: RLE can be used for data storage optimization. For example, in databases where there are repetitive patterns or sequences, RLE can be applied to reduce the storage space required.

##### hard

#### security

<a id="sec_medium"></a>

##### medium --> decode steganography
- algorithm
    - call the dell stenography function
- use cases
    - Covert Communication: Steganography can be used for covert communication in various scenarios where privacy and secrecy are crucial. For instance, it could be used by intelligence agencies or military personnel to transmit sensitive information without attracting attention. In the digital realm, steganography can be employed to hide messages within seemingly innocuous images, audio files, or even text.

    - Digital Watermarking: In the realm of copyright protection and intellectual property rights, steganography finds application in digital watermarking. Watermarks can be embedded within images, audio, or video files to assert ownership and deter unauthorized use or distribution.

    - Information Concealment in Malware: Malicious actors often use steganography to hide malicious code or instructions within seemingly innocuous files. This technique can be employed in malware to evade detection by antivirus software or to facilitate covert communication between malware components and command-and-control servers.

<a id="sec_hard"></a>

##### **hard --> DES**
- algorithm
    - implement DES from scratch 
- use cases
    - **Legacy Systems:** Some older systems may still rely on DES for encryption due to historical reasons or compatibility constraints. While not recommended for new deployments, existing systems may continue to use DES until they can be upgraded.

    - **Low-Security Applications:** In scenarios where the data being encrypted doesn't require high levels of security, DES may still be considered sufficient. For example, in certain internal communications within organizations where the risk of a sophisticated attack is low.

### Machine learning
#### easy
- algorithm:
    - Simple Exponential Smoothing (SES)
- use cases:
    - **Forecasting** is the process of estimating future trends, outcomes, or events based on historical data, patterns, and analysis. It plays a crucial role in decision-making across various domains, helping organizations plan, allocate resources, and respond to future scenarios.

#### medium
- algorithm
    - Adaboost

- **Binary Classification:** Adaboost is commonly used for binary classification problems. It can effectively classify data into two classes based on a set of features.

- **Image Classification:** Adaboost can be applied to image classification tasks, where the goal is to classify images into different categories or labels.

### Computer Vision
#### easy
