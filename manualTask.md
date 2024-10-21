# Manual Test Cases for Transaction History Tab

# Sanity Tests

## Test Case 1: Transaction History Data Display
**Goal:** Verify UI presents the backend data correctly.
- **Prerequisites:** User is connected with a wallet (MetaMask, WalletConnect etc..).
- **Steps:**
1. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab.
2. Fetch data of transaction history using API calls to retrieve directly from the backend.
3. Compare the transaction data displayed on the UI with the data from the API.
- **Expected Result:** The UI should accurately display the backend data - Date, Token, From, To, Port Fee.
UI should display correctly corresponding icons and logos of currencies.

## Test Case 2: Empty Transaction Log
**Goal:** Verify UI presents the backend data correctly.
- **Prerequisites:** User is connected with a NEW wallet (MetaMask, WalletConnect etc..) without transactions made.
- **Steps:**
1. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab.
- **Expected Result:** The UI should present Empty Transaction Log.

## Test Case 3: Pagination Functionality
**Goal:** Verify pagination navigates and present data correctly.
- **Prerequisites:** User is connected with a wallet (MetaMask, WalletConnect etc..).
- **Steps:**
1. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab.
2. Ensure you have sufficent transaction to show.
3. Navigate between pages to verify all transaction are accounted for and presented correctly.
- **Expected Result:** The UI should Navigate between transaction logs.

## Test Case 4: Wallet Connection
**Goal:** Verify transaction history displays only when the MetaMask wallet is connected.
- **Prerequisites:** User is NOT connected with a wallet.
- **Steps:**
1. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab.
2. Verify transaction history tab is empty.
3. Connect Wallet.
- **Expected Result:** Data only appears when the wallet is connected, data shown is accurate.

## Test Case 5: Date Format and Sorting Verification
**Goal:** The date follow correct format, sorting working consistently
- **Prerequisites:** User is connected with a wallet.
- **Steps:**
1. Verify the date format in the "Date" column.
2. Test sorting by ascending and descending date order.
- **Expected Result:** The date is in format of "Month Day, Year".

## Test Case 6: Download Transaction History CSV
**Goal:** The CSV file should match the UI data.
- **Prerequisites:** User is connected with a wallet.
- **Steps:**
1. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab.
2. Click the "Download Tx history CSV" button.
3. Verify that the CSV file downloads correctly and that the data matches what is displayed on the UI.
- **Expected Result:** CSV file should match the UI data.

## Test Case 7: Switching Wallets
**Goal:** Verify that switching between two valid wallets updates the transaction history accordingly.
- **Prerequisites:** User is Not connected with a wallet.
- **Steps:**
1. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab.
2. Connect Wallet A via MetaMask.
3. Verify Wallet A transactions corresponds to the data.
4. Disconnect Wallet A.
5. Connect Wallet B via WalletConnect.
6. Verify Wallet B transactions corresponds to the data.
- **Expected Result:** For Every wallet matching transaction history should be displayed.

## Test Case 8 - Negative: Wallet Not Connected
**Goal:** Verify that no data is displayed when a wallet is not connected.
- **Prerequisites:** User is logged in with no wallet.
- **Steps:**
1. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab.
- **Expected Result:** Page displays a message empty log indicating you need to collect a wallet.

## Test Case 9 - Negative: CSV Download with No Transactions
**Goal:** Verify CSV download handles cases where no transactions are presented.
- **Prerequisites:** User is connected with a NEW wallet (MetaMask, WalletConnect etc..) without transactions made.
- **Steps:**
1. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab.
2. Attempt to download CSV
- **Expected Result:** CSV file is either not generated or shows appropriate "No transactions" message.

## Test Case 10: Responsive Design and Layout for Various Devices sizes
**Goal:** UI present data and be fully responsive.
- **Prerequisites:** User is connected with a wallet.
- **Steps:**
1. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab via Desktop.
2. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab via Mobile.
3. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab via Tablet.
- **Expected Result:** The transaction table should be fully responsive, with no broken layouts. Columns should adjust dynamically, and horizontal scrolling should work smoothly on smaller devices.

## Test Case 11: Verify ChainPort app is supported by different browsers.
**Goal:** UI present data and be fully responsive.
- **Prerequisites:** User is connected with a wallet.
- **Steps:**
1. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab via Chrome.
2. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab via Edge.
3. Visit the ChainPort app using https://app.chainport.io/ and navigate to the "Transaction History" tab via FireFox.
- **Expected Result:** UI should be displayed properly.

## Test Case 12: Verify UI display properly large number of transactions
**Goal:** UI gracefully handles with large number of transactions
- **Prerequisites:** User is connected with a wallet.
- **Steps:**
1. Simulate a large number of transactions (100+ transactions).
2. Verify that the UI handles large number of transactions accurately.
- **Expected Result:** The UI should handle large numbers of transactions properly displaying them by the order of execution (Date).

## Test Case 13: Verify UI display lagre transaction volume properly.
**Goal:** UI handles large numbers gracefully
- **Prerequisites:** User is connected with a wallet.
- **Steps:**
1. Simulate a large transaction volume (100,000 tokens).
2. Verify that the UI handles large numbers accurately
- **Expected Result:** The UI should handle large numbers gracefully, ensuring that the format does not overflow or break the layout.

 ## Test Case 14: Security Test - Unauthorized Access Prevention
**Goal:** Unauthorized access should be blocked
- **Prerequisites:** User is connected with a MetaMask wallet.
- **Steps:**
1. Simulate an unauthorized user trying to access the "Transaction History" tab without connecting their wallet.
2. Test session hijacking or invalid access token scenarios.
- **Expected Result:** Unauthorized access should be blocked, and the user should be redirected to a wallet connection prompt. All transactions should be securely fetched and displayed only when a valid wallet connection is active.

