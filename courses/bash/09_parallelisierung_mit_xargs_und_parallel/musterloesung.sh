#!/usr/bin/env bash
# ==============================================================================
# Bash 09: Parallelisierung mit xargs, GNU parallel & Background Workers
# MUSTERLÖSUNG
# ==============================================================================

parallel_xargs_process() {
    local input_file="${1:-}"
    local max_procs="${2:-2}"

    if [ -z "$input_file" ] || [ ! -f "$input_file" ]; then
        return 1
    fi

    # Paralleles Ausführen via xargs
    xargs -P "$max_procs" -I {} bash -c 'echo "PROCESSED: $1"' _ {} < "$input_file"
}

background_workers_wait() {
    local tasks=("$@")

    if [ ${#tasks[@]} -eq 0 ]; then
        return 1
    fi

    local pids=()

    for task in "${tasks[@]}"; do
        (
            echo "WORKER_START: $task"
            sleep 0.02
            echo "WORKER_DONE: $task"
        ) &
        pids+=($!)
    done

    # Warten auf alle Hintergrund-Prozesse
    for pid in "${pids[@]}"; do
        wait "$pid"
    done

    echo "ALL_WORKERS_FINISHED"
    return 0
}

parallel_batch_calculator() {
    local numbers_file="${1:-}"
    local max_procs="${2:-4}"

    if [ -z "$numbers_file" ] || [ ! -f "$numbers_file" ]; then
        return 1
    fi

    # Berechne n^2 parallel und formatiere Ausgabe numerisch sortiert
    xargs -P "$max_procs" -I {} bash -c 'num="$1"; sq=$((num * num)); echo "$num^2 = $sq"' _ {} < "$numbers_file" | sort -n
}

throttle_concurrent_jobs() {
    local total_jobs="${1:-0}"
    local max_concurrent="${2:-2}"

    if [ "$total_jobs" -le 0 ]; then
        return 1
    fi

    for ((i=1; i<=total_jobs; i++)); do
        (
            echo "JOB_RUNNING: $i"
            sleep 0.05
        ) &

        # Sobald mehr oder gleich max_concurrent Jobs laufen: warten bis ein Job fertig ist
        while [ $(jobs -rp | wc -l) -ge "$max_concurrent" ]; do
            sleep 0.01
        done
    done

    # Auf verbleibende Jobs warten
    wait

    echo "THROTTLE_POOL_COMPLETED"
    return 0
}
