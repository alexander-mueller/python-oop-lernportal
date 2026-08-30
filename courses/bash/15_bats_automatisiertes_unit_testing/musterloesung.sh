#!/usr/bin/env bash
# ==============================================================================
# Bash 15: BATS Automatisiertes Unit-Testing & Mocking
# MUSTERLÖSUNG
# ==============================================================================

generate_bats_test_file() {
    local test_name="${1:-}"
    local target_cmd="${2:-}"
    local expected_exit="${3:-0}"
    local expected_text="${4:-}"

    if [ -z "$test_name" ] || [ -z "$target_cmd" ]; then
        return 1
    fi

    cat <<EOF
setup() {
    # Optional setup logic
    true
}

@test "$test_name" {
    run $target_cmd
    [ "\$status" -eq $expected_exit ]
    [[ "\$output" =~ "$expected_text" ]]
}
EOF
}

create_executable_mock() {
    local mock_dir="${1:-}"
    local cmd_name="${2:-}"
    local exit_code="${3:-0}"
    local output_text="${4:-}"

    if [ -z "$mock_dir" ] || [ -z "$cmd_name" ]; then
        return 1
    fi

    mkdir -p "$mock_dir"
    local mock_file="${mock_dir}/${cmd_name}"

    cat <<EOF > "$mock_file"
#!/usr/bin/env bash
echo "$output_text"
exit $exit_code
EOF

    chmod +x "$mock_file"
    return 0
}

parse_tap_test_summary() {
    local tap_stream="${1:-}"

    if [ -z "$tap_stream" ]; then
        return 1
    fi

    local passed=0
    local failed=0

    while IFS= read -r line; do
        if [[ "$line" =~ ^not\ ok\ [0-9]+ ]]; then
            ((failed++))
        elif [[ "$line" =~ ^ok\ [0-9]+ ]]; then
            ((passed++))
        fi
    done <<< "$tap_stream"

    local total=$((passed + failed))
    echo "TOTAL: $total | PASSED: $passed | FAILED: $failed"
}

run_sandboxed_test_runner() {
    local test_cmd="${1:-}"
    local mock_dir="${2:-}"

    if [ -z "$test_cmd" ] || [ -z "$mock_dir" ]; then
        return 1
    fi

    local status=0
    local output=""

    output=$(
        export PATH="${mock_dir}:${PATH}"
        eval "$test_cmd" 2>&1
    ) || status=$?

    # Zeilenumbrüche für einzeilige Zusammenfassung bereinigen
    output=$(echo "$output" | tr '\n' ' ' | sed 's/[[:space:]]*$//')

    echo "STATUS: $status | OUTPUT: $output"
    return 0
}
