# Video RAG Search Pipeline

A streamlined Retrieval-Augmented Generation (RAG) system for searching and analyzing video content using Google Vertex AI. This pipeline extracts metadata from video files and creates an intelligent search interface **without requiring CSV intermediate steps**.

## 🎯 Features

- **Direct Upload Approach**: No CSV files needed - uploads directly to RAG corpus
- **Smart Video Analysis**: Extracts metadata from filenames and content
- **Multilingual Support**: Handles English and Bahasa Indonesia content
- **Content Classification**: Automatically categorizes romance/drama, sports, and news content
- **Optimized Search**: Low similarity threshold for better context retrieval
- **Ready-to-Use**: Simple functions for immediate video content search

## 📊 Supported Content Types

### 🎭 Romance/Drama Series
- **"Cinta Sedalam Rindu"** episodes with character analysis (Aluna, Galaxy, Ezra, Felicia)
- Episode number extraction and character relationship mapping
- Automatic keyword generation in English and Indonesian

### ⚽ Sports Highlights
- **Indonesian football/soccer** match highlights
- Team extraction (Persebaya, Arema FC, Persija, etc.)
- Match week information (Pekan 13, 14, etc.)
- Sports-specific metadata and keywords

### 📺 News Reports
- **Liputan 6** news coverage
- Current affairs and journalism content
- Event-based categorization and analysis

## 🚀 Quick Start

### Prerequisites
- Google Cloud Project with Vertex AI API enabled
- Video files in a local directory
- Python environment with required packages

### Installation
```bash
pip install google-cloud-aiplatform google-cloud-storage google-genai pandas pathlib
```

### Usage

1. **Configure your project settings**:
```python
PROJECT_ID = "your-project-id"  # Update this
VIDEO_FOLDER = "video"          # Update this path
```

2. **Run the complete pipeline**:
   - Extract video metadata
   - Create RAG corpus
   - Upload analysis directly (no CSV!)
   - Create search interface

3. **Search your content**:
```python
# Search for specific content
search_videos("What romance videos do we have?")
search_videos("Show me sports highlights from Pekan 13")
search_videos("Which videos have episode information?")

# Test the system
test_search_system()
```

## 📁 Dataset Files

This repository includes sample datasets for testing and evaluation:

### `GoldenSet.csv`
- **30 test queries** for evaluation
- **Query types**: Soap opera, Sports, News
- **Difficulty levels**: Easy, Medium
- **Languages**: English and Indonesian queries
- **Expected answers** for quality assessment

### `video_metadata_analysis.csv` *(Optional Reference)*
- Sample output format showing metadata extraction results
- 52 entries with comprehensive video analysis
- Includes embeddings and content classification
- **Note**: The new pipeline doesn't require CSV - this is for reference only

## 🏗️ Architecture

### Traditional RAG Approach:
```
Video Files → Metadata → CSV → Cloud Storage → RAG Import → Search
```

### Our Streamlined Approach:
```
Video Files → Metadata → Direct RAG Upload → Search
```

## 💡 Key Benefits

- ✅ **No CSV intermediate files** - saves storage and complexity
- ✅ **50% fewer processing steps** - faster pipeline
- ✅ **Direct metadata control** - better file organization
- ✅ **Optimized retrieval settings** - improved search accuracy
- ✅ **Simple debugging** - easier troubleshooting

## 📝 Example Queries

### Romance/Drama Content:
- "Show me videos about Aluna and Galaxy"
- "Which episodes have character relationships?"
- "What romance drama content is available?"

### Sports Content:
- "Find football highlights from this week"
- "Show me matches between Persebaya and Arema"
- "What sports content do we have?"

### News Content:
- "Tell me about recent news videos"
- "Show me Liputan 6 coverage"
- "What current affairs content is available?"

## 🔧 Technical Details

### RAG Configuration:
- **Embedding Model**: `text-multilingual-embedding-002`
- **Similarity Threshold**: 0.1 (optimized for better retrieval)
- **Top-K Results**: 15 (comprehensive context)
- **Chunk Size**: 1000 tokens with 200 overlap

### Content Analysis:
- **Filename parsing** for metadata extraction
- **Character recognition** for drama series
- **Team and match extraction** for sports
- **Event categorization** for news

### Search Optimization:
- **Enhanced query expansion** with multilingual terms
- **Context-aware retrieval** with fallback strategies
- **Specific metadata inclusion** in responses

## 🎬 Video Analysis Pipeline

1. **Metadata Extraction**: Smart analysis of video filenames
2. **Content Classification**: Automatic genre and type detection
3. **Keyword Generation**: Multilingual searchable terms
4. **Direct Upload**: Stream to RAG corpus without CSV
5. **Search Interface**: Optimized retrieval and generation

## 📈 Performance

The streamlined approach provides:
- **Faster processing**: Direct upload eliminates conversion steps
- **Better accuracy**: Optimized similarity thresholds
- **Improved organization**: Individual file tracking
- **Enhanced debugging**: Clear error isolation

## 🛠️ Customization

### Adding New Content Types:
Extend the `analyze_filename_content()` function to support additional video categories.

### Adjusting Search Parameters:
Modify retrieval configuration in `create_search_interface()` for your specific needs.

### Enhanced Video Analysis:
The pipeline supports Gemini API integration for actual video content analysis beyond filename parsing.

## 📋 File Structure

```
├── Rag_search.ipynb         # Main pipeline notebook
├── GoldenSet.csv           # Test queries dataset
├── video_metadata_analysis.csv  # Sample output reference
└── README.md              # This documentation
```

## 🎯 Use Cases

- **Media Content Management**: Organize and search video libraries
- **Educational Content**: Find specific episodes or topics
- **Sports Analysis**: Search match highlights and statistics
- **News Monitoring**: Track coverage and events
- **Content Discovery**: Intelligent video recommendation

## 🚀 Getting Started

1. Clone this repository
2. Open `Rag_search.ipynb` in Jupyter
3. Configure your Google Cloud project settings
4. Add your video files to the specified folder
5. Run all cells to create your RAG search system
6. Start searching with `search_videos("your question")`

---

**Note**: This pipeline is designed for educational and demonstration purposes. Ensure you have proper permissions for your video content and comply with relevant data usage policies.