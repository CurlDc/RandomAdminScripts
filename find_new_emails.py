import argparse
import pandas

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Small script to see what emails we need to add to google groups from curling manager exports')
    parser.add_argument('-c', '--curling-manager-input',
                         help='Path to CSV exported from Curling Manager',
                         required=True)
    parser.add_argument('-g', '--google-group-input',
                         help='Path to CSV exported from Google group member list',
                         required=True)
    args = parser.parse_args()

    cm_emails = pandas.read_csv(args.curling_manager_input).Email
    gg_emails = pandas.read_csv(args.google_group_input)['Email address']

    cm_emails = map(str.lower, cm_emails)
    gg_emails = map(str.lower, gg_emails)

    print('New emails to add to google group:')
    for email in set(cm_emails).difference(gg_emails):
        print(f'\t{email}')
