
# Stock Market Prediction Using Liquid Neural Networks

This project focuses on predicting the stock prices of Tesla (TSLA) and Apple (AAPL) using advanced machine learning techniques, specifically Liquid Neural Networks (LNN). The goal is to leverage historical stock data to forecast future prices with high accuracy.
![User Interface](https://github.com/HusseinJammal/Liquid-Neural-Networks-in-Stock-Market-Prediction/assets/82166319/a9cb59a3-a9cf-4ec0-bfb7-a0a974b5cdee)

## Project Structure

```
Liquid-Neural-Networks/
├── README.md                              # Project documentation
├── LICENSE                                # MIT License
├── app.py                                 # Flask backend API
├── tesla_best_model_lnn_2 (1).h5         # Pre-trained Tesla model
├── apple_best_model_lnn_2 (2) (1).h5     # Pre-trained Apple model
└── stock/                                 # React frontend application
    ├── public/                            # Static assets
    ├── src/                              # React source code
    ├── package.json                      # Node.js dependencies
    └── README.md                         # React app documentation
```

**Key Components:**
-   **Data Collection**: Data is sourced from Yahoo Finance using the `yfinance` library, covering daily stock movements from specific start dates up to the present.
-   **Exploratory Data Analysis (EDA)**: Includes candlestick plots with moving averages, correlation heatmaps, box plots, and histograms of daily price changes.
-   **Feature Engineering**: Development of multiple technical indicators to enrich the model's input features.
-   **Model Architecture**: Utilization of Liquid Neural Networks model to predict adjusted close prices.
-   **Evaluation**: Assessment of model performance using metrics like MSE, RMSE, MAE, MAPE, and Directional Accuracy.
-   **Web Interface**: React-based frontend for interactive stock prediction with Flask API backend.

## Data


The data for this project is retrieved from Yahoo Finance, focusing on the following stocks:

-   **Apple (AAPL)**: From 2010-01-01 to yesterday.
-   **Tesla (TSLA)**: From 2010-06-29 to yesterday.

Features included are Open, High, Low, Close, Adjusted Close, and Volume. Technical indicators such as MACD, RSI, Bollinger Bands, and others are calculated to enhance the dataset.

## Setup and Installation

To run this project on your local machine, follow these steps:

### Prerequisites

Ensure you have the following installed on your machine:
- **Python 3.7+** with pip
- **Node.js 14+** with npm

### Required Python Libraries

```bash
pip install flask flask-cors pandas-datareader yfinance pandas-ta pandas numpy scikit-learn tensorflow
```

**Complete dependency list:**
- `flask` - Web framework for API
- `flask-cors` - Cross-Origin Resource Sharing support
- `pandas-datareader` - Financial data access
- `yfinance` - Yahoo Finance data
- `pandas-ta` - Technical analysis indicators
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `scikit-learn` - Machine learning utilities
- `tensorflow` - Deep learning framework

### Installation Steps

1.  Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ajaygm18/Liquid-Neural-Networks.git
    cd Liquid-Neural-Networks
    ```

2.  Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Or install manually:
    ```bash
    pip install flask flask-cors pandas-datareader yfinance pandas-ta pandas numpy scikit-learn tensorflow
    ```

3.  Navigate to the React application directory:

    ```bash
    cd stock
    ```

4.  Install Node.js dependencies:

    ```bash
    npm install
    ```

5.  Start the React frontend application:

    ```bash
    npm start
    ```

6.  In a separate terminal, navigate back to the root directory and run the Python Flask backend:

    ```bash
    cd ..
    python app.py
    ```

The React application will be available at `http://localhost:3000` and the Flask API will be running on `http://localhost:5000`.

## Feature Engineering


Detailed feature engineering steps include the creation of:

-   Moving Averages (14 & 21 days for MACD, etc.)
-   Pivot Points, Momentum, and Volatility Indices like ATR and Bollinger Bands
-   Volume indicators like On Balance Volume
-   Oscillators such as Stochastic Indicators
-   Fibonacci Retracement Levels

## Models


### Liquid Neural Networks

Utilization of LNN with configurations for different layers, including dropout and regularization to prevent overfitting.

### Pre-trained Models

The repository includes pre-trained models for:
- **Tesla (TSLA)**: `tesla_best_model_lnn_2 (1).h5`
- **Apple (AAPL)**: `apple_best_model_lnn_2 (2) (1).h5`

## API Usage

The Flask backend provides the following endpoints:

### `/predict` (GET/POST)
Predicts the next day's adjusted close price for a given stock.

**Parameters:**
- `stock_name`: Either 'TSLA' or 'AAPL'
- Date range parameters for historical data fetching

**Response:**
Returns the predicted adjusted close price as a string value.

### Example Usage

```bash
# Using curl to get a prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"stock_name": "TSLA"}'
```


## Evaluation


The models are evaluated using the following metrics:

-   MSE (Mean Squared Error)
-   RMSE (Root Mean Squared Error)
-   MAE (Mean Absolute Error)
-   MAPE (Mean Absolute Percentage Error)
-   Directional Accuracy

Results from these metrics provide insights into the models' predictive accuracy and performance.

## Troubleshooting

### Common Issues

1. **Model files not found**: Ensure the `.h5` model files are in the root directory
2. **CORS errors**: Make sure the Flask backend is running on port 5000
3. **Module import errors**: Verify all Python dependencies are installed
4. **React app not starting**: Ensure you're in the `stock` directory when running `npm start`

### Python Environment

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt  # After creating requirements.txt
```

## Contributions

Contributions to this project are welcome! Here's how you can contribute:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Make your changes** and test them thoroughly
4. **Commit your changes**: `git commit -m 'Add some feature'`
5. **Push to the branch**: `git push origin feature/your-feature`
6. **Submit a pull request**

Please ensure your code follows the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
