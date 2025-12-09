import dns.resolver
import os

INPUT_FILE = 'emails.txt'

def load_emails(filename):
    if not os.path.exists(filename):
        print(f'Файл {filename} не найден.')
        return []

    with open(filename, 'r', encoding='utf-8') as f:
        emails = [line.strip() for line in f if line.strip()]
    return emails

def check_domain(domain):
    try:
        try:
            dns.resolver.resolve(domain, 'A')
        except dns.resolver.NoAnswer:
            dns.resolver.resolve(domain, 'AAAA')
    except dns.resolver.NXDOMAIN:
        return 'домен отсутствует'
    except Exception:
        return 'MX-записи отсутствуют или некорректны'

    # Проверяем MX-записи
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        if mx_records:
            return 'домен валиден'
    except Exception:
        return 'MX-записи отсутствуют или некорректны'

    return 'MX-записи отсутствуют или некорректны'


if __name__ == '__main__':
    emails = load_emails(INPUT_FILE)

    if not emails:
        print('Список email пуст или файл отсутствует.')
        exit()

    for email in emails:
        if '@' not in email:
            print(f'{email}: некорректный email')
            continue

        domain = email.split('@')[1]
        status = check_domain(domain)
        print(f'{email}: {status}')
