#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 12: DMARC & E-MAIL-SECURITY SUITE
# ==============================================================================

format_dmarc_record() {
  local dom="$1"
  local pol="$2"
  local rua="$3"
  local pct="${4:-100}"

  dom="${dom%.}"
  local fqdn="_dmarc.${dom}."

  printf "%-25s %-7s IN  TXT \"v=DMARC1; p=%s; rua=mailto:%s; pct=%s\"\n" "$fqdn" "3600" "$pol" "$rua" "$pct"
  return 0
}

evaluate_dmarc_verdict() {
  local spf="$1"
  local dkim="$2"
  local pol="$3"

  if [ "$spf" = "true" ] || [ "$dkim" = "true" ]; then
    echo "VERDICT_PASS: Zustellung im Posteingang (mindestens ein Mechanismus valide)."
    return 0
  fi

  case "$pol" in
    none)
      echo "VERDICT_FAIL_DELIVER: Fehlgeschlagen, aber p=none -> Zustellung erfolgt dennoch."
      return 0
      ;;
    quarantine)
      echo "VERDICT_QUARANTINE: Fehlgeschlagen -> Mail in SPAM-Ordner verschieben."
      return 1
      ;;
    reject)
      echo "VERDICT_REJECT: Fehlgeschlagen -> Mail an SMTP-Pforte abweisen (550 DMARC Failed)!"
      return 1
      ;;
    *)
      echo "UNKNOWN_POLICY"
      return 1
      ;;
  esac
}

audit_email_security_suite() {
  local spf="$1"
  local dkim="$2"
  local dmarc="$3"

  local score=0

  # SPF
  if [[ "$spf" =~ -all ]]; then
    score=$((score + 30))
  elif [[ "$spf" =~ ~all ]]; then
    score=$((score + 15))
  fi

  # DKIM
  if [[ "$dkim" =~ v=DKIM1 ]] && [[ "$dkim" =~ p= ]]; then
    score=$((score + 35))
  fi

  # DMARC
  if [[ "$dmarc" =~ p=reject ]]; then
    score=$((score + 35))
  elif [[ "$dmarc" =~ p=quarantine ]]; then
    score=$((score + 25))
  elif [[ "$dmarc" =~ p=none ]]; then
    score=$((score + 10))
  fi

  local grade="INSECURE"
  if [ "$score" -ge 90 ]; then
    grade="EXCELLENT"
  elif [ "$score" -ge 60 ]; then
    grade="ACCEPTABLE"
  fi

  echo "SCORE=$score | RATING=$grade"
  return 0
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  format_dmarc_record "$@"
fi
