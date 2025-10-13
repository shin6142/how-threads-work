#!/bin/bash

# --- 設定 ---
URL="http://127.0.0.1:3000/test"
CONCURRENCY=1000     # C: 同時リクエスト数
TOTAL_REQUESTS=1000   # N: 総リクエスト数
TIMEOUT=20          # abのタイムアウトを20秒に設定

# 負荷テストを実行する関数
function run_test() {
    local mode_name=$1
    echo -e "\n--- 負荷テスト実行 (N=${TOTAL_REQUESTS}, C=${CONCURRENCY}) ---"
    
    # abを実行
    ab -n $TOTAL_REQUESTS -c $CONCURRENCY -t $TIMEOUT $URL 2>&1
    
    echo "--- $mode_name テスト完了 ---"
}

# --- 検証開始 ---
run_test "スレッド"