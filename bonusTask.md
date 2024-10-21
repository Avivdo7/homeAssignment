# Functional Test Cases
## Context:
- **Protocols:** ChainPortX and CCTP
- **Chains:** ETHEREUM (ChainPortX & CCTP), Avalanche (CCTP), Optimism (ChainPortX & CCTP)
- **Threshold:** When the ported amount is below or above a defined threshold range, the CCTP protocol is used. If within threshold range and the chain supports ChainPortX use it, otherwise CCTP.

## Test Case 1: Verify Amount within Threshold range select ChainPortX (using Ethereum)
**Goal:** Verify ChainPortX protocol selected automatically
- **Prerequisites:** User is connected with a wallet and selects Ethereum's chain.
- **Steps:**
1. Port an amount within the threshold range.
- **Expected Result:** The ChainPortX protocol should be selected

## Test Case 2: Verify Amount Below Threshold select CCTP (using Ethereum)
**Goal:** Verify CCTP protocol selected automatically
- **Prerequisites:** User is connected with wallet and selects Ethereum's chain.
- **Steps:**
1. Port an amount below the threshold.
- **Expected Result:** The CCTP protocol should be selected.

## Test Case 3: Verify Amount Above Threshold select CCTP (using Ethereum)
**Goal:** Verify CCTP protocol selected automatically
- **Prerequisites:** User is connected with wallet and selects Ethereum's chain.
- **Steps:**
1. Port an amount above the threshold.
- **Expected Result:** The CCTP protocol should be selected.

## Test Case 4: Verify Amount within Threshold range select CCTP (using Avalanche)
**Goal:** Verify CCTP protocol selected automatically
- **Prerequisites:** User is connected with a wallet and selects Avalanche's chain.
- **Steps:**
1. Port an amount within the threshold range.
- **Expected Result:** The CCTP protocol should be selected.

## Test Case 5: Verify Amount Below Threshold select CCTP (using Avalanche)
**Goal:** Verify CCTP protocol selected automatically
- **Prerequisites:** User is connected with wallet and selects Avalanche's chain.
- **Steps:**
1. Port an amount below the threshold.
- **Expected Result:** The CCTP protocol should be selected.

## Test Case 6: Verify Amount Above Threshold select CCTP (using Avalanche)
**Goal:** Verify CCTP protocol selected automatically
- **Prerequisites:** User is connected with wallet and selects Avalanche's chain.
- **Steps:**
1. Port an amount above the threshold.
- **Expected Result:** The CCTP protocol should be selected.

## Test Case 7: Verify Amount within Threshold range select ChainPortX (using Optimism)
**Goal:** Verify ChainPortX protocol selected automatically
- **Prerequisites:** User is connected with a wallet and selects Optimism's chain.
- **Steps:**
1. Port an amount within the threshold range.
- **Expected Result:** The ChainPortX protocol should be selected.

## Test Case 8: Verify Amount Below Threshold select CCTP (using Optimism)
**Goal:** Verify CCTP protocol selected automatically
- **Prerequisites:** User is connected with wallet and selects Optimism's chain.
- **Steps:**
1. Port an amount below the threshold.
- **Expected Result:** The CCTP protocol should be selected.

## Test Case 9: Verify Amount Above Threshold select CCTP (using Optimism)
**Goal:** Verify CCTP protocol selected automatically
- **Prerequisites:** User is connected with wallet and selects Optimism's chain.
- **Steps:**
1. Port an amount above the threshold.
- **Expected Result:** The CCTP protocol should be selected.

## Test Case 10: Verify Fee for CCTP Protocol over Ethereum chain
**Goal:** CCTP ensures the appropriate fee is applied.
- **Prerequisites:** User is connected with a wallet and selects Ethereum's chain.
- **Steps:**
1. Port an amount below the threshold and verify the fee applied.
- **Expected Result:** The CCTP protocol must accurately enforce the appropriate fee structure.
- **Note:** Repeat step 1 with amount above threshold.

## Test Case 11: Verify Fee for ChainPortX Protocol over Ethereum chain
**Goal:** ChainPortX ensures the appropriate fee is applied.
- **Prerequisites:** User is connected with a wallet and selects Ethereum's chain.
- **Steps:**
1. Port the amount within the threshold and verify the fee applied.
- **Expected Result:** The ChainPortX protocol must accurately enforce the appropriate fee structure.


## Test Case 12: Verify Fee for CCTP Protocol over Avalanche chain
**Goal:** CCTP ensures the appropriate fee is applied.
- **Prerequisites:** User is connected with a wallet and selects Avalanche's chain.
- **Steps:**
1. Port an amount below the threshold and verify the fee applied.
- **Expected Result:** The CCTP protocol must accurately enforce the appropriate fee structure.
- **Note:** Repeat step 1 with amount above threshold.

## Test Case 13: Verify Fee for CCTP Protocol over Optimism chain
**Goal:** CCTP ensures the appropriate fee is applied.
- **Prerequisites:** User is connected with a wallet and selects Optimism's chain.
- **Steps:**
1. Port an amount below the threshold and verify the fee applied.
- **Expected Result:** The CCTP protocol must accurately enforce the appropriate fee structure.
- **Note:** Repeat step 1 with amount above threshold.

## Test Case 14: Verify Fee for ChainPortX Protocol over Optimism chain
**Goal:** ChainPortX ensures the appropriate fee is applied.
- **Prerequisites:** User is connected with a wallet and selects Optimism's chain.
- **Steps:**
1. Port an amount witin the threshold range and verify the fee applied.
- **Expected Result:** The ChainPortX protocol must accurately enforce the appropriate fee structure.