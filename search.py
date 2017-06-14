import optparse
import Evtx.Evtx as evtx

def main():
    opts = get_options()
    search(opts)


def get_options():
    option_list = [
        optparse.make_option("-f", "--file", dest="file", help="the path to log file"),
        optparse.make_option("-p", "--pattern", dest="pattern", help="the search pattern")
    ]
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage=usage, option_list=option_list)
    opts, args = parser.parse_args()
    if not opts.file or not opts.pattern:
        raise ValueError("Path is required")
    return opts


def search(opts):
    with evtx.Evtx(opts.file.strip()) as log:
        for chunk in log.chunks():
            for record in chunk.records():
                xml = record.xml()
                pattern = opts.pattern.strip()
                if(pattern in xml):
                    print(xml)


main()