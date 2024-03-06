# Pseudocode of duty
# table of content
- [welcome](#welcome)
- [team](#team)
- [fox](#fox)
    - [strategy]()
    - [riddles]()
    - [fox challenges]()
- [eagle]()
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
    - 
- use cases
Image Compression: In image processing, RLE can be used to compress bitmap images. For example, in black and white images where consecutive pixels have the same color, RLE can represent these runs of pixels with a count and the color value, reducing the size of the image data.

Text Compression: RLE can be applied to compress text files, especially those containing long sequences of repeated characters or symbols. For example, in DNA sequencing where long sequences of the same nucleotide base are common, RLE can significantly reduce the size of the data.

Network Protocols: RLE can be used in network protocols to compress data before transmission over a network. For instance, in video streaming, RLE can compress frames by encoding consecutive pixels of the same color.

Storage Optimization: RLE can be used for data storage optimization. For example, in databases where there are repetitive patterns or sequences, RLE can be applied to reduce the storage space required.

Fax Transmission: RLE was commonly used in fax transmission protocols to compress black-and-white images before sending them over the phone lines. Fax machines would encode consecutive pixels with the same color value as a count and a color value, reducing transmission time and cost.

Graphic File Formats: Some graphic file formats, such as BMP and TIFF, use RLE compression for encoding image data. This compression method is particularly effective for images with large areas of uniform color.

Run-Length Encoding of Audio: In audio processing, RLE can be applied to compress audio data. For example, in MIDI files where consecutive musical notes of the same pitch and duration occur, RLE can represent these sequences efficiently.

