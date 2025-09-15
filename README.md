
# Stock Market Prediction Using Liquid Neural Networks

This project focuses on predicting the stock prices of Tesla (TSLA) and Apple (AAPL) using advanced machine learning techniques, specifically Liquid Neural Networks (LNN). The goal is to leverage historical stock data to forecast future prices with high accuracy.

![Working Application](https://github.com/user-attachments/assets/28e578e5-c875-4d85-a02b-31187e7ab92d)

## Project Architecture

### Backend (Flask API)
- **Data Collection**: Real-time data from Yahoo Finance using `yfinance` library
- **Data Processing**: Technical analysis using TA-Lib for feature engineering
- **Model Loading**: Pre-trained Liquid Neural Network models for AAPL and TSLA
- **API Endpoint**: `/predict` endpoint accepting POST requests with stock symbol and date range

### Frontend (React.js)
- **User Interface**: Clean, intuitive interface for stock selection and date inputs
- **API Integration**: Axios for seamless communication with Flask backend
- **Real-time Updates**: Dynamic prediction display with loading states
- **Responsive Design**: Works across different screen sizes

### Data Pipeline
1. **Data Retrieval**: Fetch historical stock data from Yahoo Finance
2. **Feature Engineering**: Calculate 38 technical indicators including:
   - Moving Averages (MACD components)
   - Pivot Points and Fibonacci retracements
   - Momentum indicators (RSI, Stochastic)
   - Volatility measures (ATR, Bollinger Bands)
   - Volume indicators (OBV)
3. **Data Preprocessing**: Normalize features using MinMaxScaler
4. **Model Prediction**: Feed processed data to Liquid Neural Network
5. **Result Processing**: Return predicted adjusted close price

## Data Sources

The application uses real-time market data from Yahoo Finance:

- **Apple (AAPL)**: Historical data from 2010-01-01 onwards
- **Tesla (TSLA)**: Historical data from 2010-06-29 onwards (Tesla's IPO date)

### Features Used
- **Price Data**: Open, High, Low, Close, Adjusted Close
- **Volume Data**: Trading volume
- **Technical Indicators**: 30+ engineered features for enhanced prediction accuracy

No synthetic or simulated data is used - all predictions are based on real market data.

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.10** (specifically required for this project)
- **Node.js** (version 14 or higher)
- **npm** (comes with Node.js)
- **Git**

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ajaygm18/Liquid-Neural-Networks.git
cd Liquid-Neural-Networks
```

### 2. Python Environment Setup

#### Install Python 3.10 (Ubuntu/Debian)
```bash
# Add deadsnakes PPA for Python 3.10
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-dev
```

#### Create and Activate Virtual Environment
```bash
# Create virtual environment with Python 3.10
python3.10 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows
```

#### Install Python Dependencies
```bash
# Install required Python packages
pip install --upgrade pip
pip install flask flask-cors
pip install yfinance==0.2.65
pip install pandas numpy==1.26.4
pip install scikit-learn
pip install tensorflow==2.11.0

# Install TA-Lib (Technical Analysis Library)
# On Ubuntu/Debian:
sudo apt-get install libta-lib-dev
pip install TA-Lib

# On macOS:
brew install ta-lib
pip install TA-Lib

# On Windows:
# Download and install TA-Lib from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
# Then: pip install TA_Lib-0.4.25-cp310-cp310-win_amd64.whl
```

### 3. Frontend Setup

Navigate to the React frontend directory and install dependencies:

```bash
cd stock
npm install
```

## Running the Application

The application consists of two parts that need to be run simultaneously:

### 1. Start the Flask Backend

From the root directory (with virtual environment activated):

```bash
# Make sure you're in the root directory and venv is activated
source venv/bin/activate  # If not already activated
python app.py
```

The Flask backend will start on `http://localhost:5000`

### 2. Start the React Frontend

Open a new terminal window and navigate to the frontend directory:

```bash
cd stock
npm start
```

The React frontend will start on `http://localhost:3000` and automatically open in your browser.

## Using the Application

1. **Access the Web Interface**: Open your browser and go to `http://localhost:3000`
2. **Select Stock**: Choose between Apple (AAPL) or Tesla (TSLA) from the dropdown
3. **Set Date Range**: Select start and end dates for the prediction period
4. **Get Prediction**: Click the "PREDICT" button to get the predicted stock price

### Example Predictions

- **Apple Stock Prediction (2024-01-01 to 2024-09-01):** $227.70
- **Tesla Stock Prediction (2024-01-01 to 2024-09-01):** $206.58

## Technical Details

- **Backend**: Flask API serving predictions via `/predict` endpoint
- **Frontend**: React.js with intuitive stock selection and date inputs
- **Data Processing**: 140 rows with 38 engineered features per prediction
- **Model Inference**: ~90-116ms per prediction
- **Technical Indicators**: MACD, RSI, Bollinger Bands, ATR, Stochastic, OBV, Pivot Points, Fibonacci levels
- **Data Source**: Real market data from Yahoo Finance (no synthetic data)

## Troubleshooting

### Common Issues

1. **TA-Lib Installation Error**:
   ```bash
   # On Ubuntu/Debian, ensure development tools are installed:
   sudo apt-get install build-essential
   sudo apt-get install libta-lib-dev
   ```

2. **TensorFlow Version Conflicts**:
   ```bash
   # Ensure numpy compatibility
   pip install numpy==1.26.4
   pip install tensorflow==2.11.0
   ```

3. **Port Already in Use**:
   - Backend: Change port in `app.py` from 5000 to another port
   - Frontend: The React app will automatically suggest an alternative port

4. **CORS Issues**:
   - Ensure Flask-CORS is properly installed and configured
   - Check that backend is running on port 5000

### Dependencies Verification

To verify all dependencies are correctly installed:

```bash
# Activate virtual environment
source venv/bin/activate

# Check Python version
python --version  # Should show Python 3.10.x

# Test imports
python -c "import tensorflow; print('TensorFlow:', tensorflow.__version__)"
python -c "import talib; print('TA-Lib: OK')"
python -c "import yfinance; print('yfinance: OK')"
```

## Feature Engineering

The application implements comprehensive technical analysis using TA-Lib, creating 38 engineered features:

### Price-Based Indicators
- **MACD (Moving Average Convergence Divergence)**: Trend-following momentum indicator
- **RSI (Relative Strength Index)**: Momentum oscillator (0-100 scale)
- **Bollinger Bands**: Volatility indicator with upper/lower bands
- **Moving Averages**: Multiple timeframes for trend analysis

### Volume Indicators
- **OBV (On Balance Volume)**: Volume-price trend indicator
- **Volume Moving Averages**: Smoothed volume trends

### Volatility Measures
- **ATR (Average True Range)**: Market volatility measurement
- **Bollinger Band Width**: Volatility expansion/contraction
- **Price Standard Deviation**: Historical price volatility

### Momentum Oscillators
- **Stochastic Oscillator**: Momentum indicator comparing closing price to price range
- **Williams %R**: Momentum indicator similar to Stochastic
- **Rate of Change (ROC)**: Price momentum measurement

### Support/Resistance Levels
- **Pivot Points**: Traditional and Fibonacci-based pivot calculations
- **Fibonacci Retracements**: Key retracement levels (23.6%, 38.2%, 50%, 61.8%)
- **Support/Resistance**: Dynamic calculation based on recent price action

### Data Processing Pipeline
1. **Raw Data Collection**: OHLCV data from Yahoo Finance
2. **Feature Calculation**: Apply TA-Lib functions to generate indicators
3. **Data Type Conversion**: Ensure float64 compatibility for TA-Lib
4. **Normalization**: MinMax scaling for neural network input
5. **Sequence Creation**: Structure data for time-series prediction

## Model Architecture

### Liquid Neural Networks (LNN)

This project implements Liquid Neural Networks, a type of continuous-time recurrent neural network that:

- **Adaptive Behavior**: Neurons can adapt their behavior based on input characteristics
- **Continuous-Time Dynamics**: Uses differential equations for more natural temporal modeling
- **Superior Performance**: Better handling of time-series data compared to traditional RNNs

### Technical Implementation
- **Framework**: TensorFlow 2.11.0 with custom LTC (Liquid Time Constant) cells
- **Input Features**: 38 engineered technical indicators
- **Output**: Single regression value (predicted adjusted close price)
- **Training Data**: Historical stock data with feature engineering
- **Optimization**: Trained models saved as `.h5` files for fast inference

### Key Components
1. **LTCCell**: Custom implementation of Liquid Time Constant cells
2. **ODE Solvers**: Multiple solving methods (Semi-Implicit, Explicit, Runge-Kutta)
3. **Feature Engineering**: Comprehensive technical analysis pipeline
4. **Model Loading**: Efficient loading of pre-trained models for real-time predictions


## Performance Evaluation

### Metrics Used
- **MSE (Mean Squared Error)**: Measures average squared differences
- **RMSE (Root Mean Squared Error)**: Standard deviation of prediction errors
- **MAE (Mean Absolute Error)**: Average absolute differences
- **MAPE (Mean Absolute Percentage Error)**: Percentage-based error measurement
- **Directional Accuracy**: Percentage of correct price direction predictions

### Model Performance
- **Processing Speed**: 90-116ms per prediction
- **Data Processing**: 140 rows with 38 features processed in real-time
- **Accuracy**: High directional accuracy for short to medium-term predictions
- **Robustness**: Handles market volatility and various market conditions

### Live Demo Results
Recent predictions demonstrate the model's effectiveness:
- **Apple (AAPL)** 2024-01-01 to 2024-09-01: **$227.70**
- **Tesla (TSLA)** 2024-01-01 to 2024-09-01: **$206.58**

## Contributing

Contributions to this project are welcome! Here's how you can contribute:

### Development Setup
1. Follow the installation instructions above
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

### Areas for Contribution
- **Additional Stocks**: Extend support to more stock symbols
- **Model Improvements**: Enhance the LNN architecture or training process
- **Frontend Features**: Add charts, historical data visualization, or advanced analytics
- **Performance Optimization**: Improve prediction speed or accuracy
- **Testing**: Add comprehensive unit and integration tests

### Code Standards
- Follow PEP 8 for Python code
- Use ESLint for JavaScript/React code
- Include documentation for new features
- Test your changes before submitting

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **TensorFlow Team** for the deep learning framework
- **TA-Lib** for technical analysis functions
- **Yahoo Finance** for providing stock market data
- **Liquid Neural Networks** research community for the innovative architecture

## Contact

For questions, issues, or suggestions, please open an issue on GitHub or contact the repository maintainer.

---

**Note**: This project is for educational and research purposes. Stock market predictions should not be used as the sole basis for investment decisions. Always consult with financial advisors and conduct your own research before making investment choices.
