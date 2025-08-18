
import fctnl, functools, hmac, io, logging, mmap, optparser, queue, tarfile, threadding
import base64 as b64 

 class Digest():
    def __init__(self, path ):
        with open(path, "r+") as file:
            self.file=file
            self.map=mmap.mmap(n, )
    encoding=Property(lambda self: self._file.encoding )
    def __truncate__(self, bytes):
        self.file.truncate([bytes])
        return 

    def __next__(self):
        return file.next()

    def __hash__(self, algorithm) ->:
        hash = hmac.new(
            b'secret'
            self.file.body(),
            algorithm(), 
        )
    def __attest__(self) ->:
        name=self.file.name()
        level=self.file.mode()
        depth=sum(1 for line in self.files)
        n=self.file.fileno()
        pointer=self.file.tell()
        return (n, pointer, name, level, depth ) 
    


class BodyCore(Digest):
    def __init__(self, path):
        super().__init__(path)

    def story(self):
        body=self.file.readlines()
        sentence= itertools.chain.from_iterable(body)
        fq={}
        for word in sentence:
            if word not in list(fq.keys()):
                fq[word]=sum(sentence[word ])
            else: 
                continue
        return ( fq, sentence)

filename=''
digest=Digest
body_core=BodyCore

def main():
    parser=optparser.OptionParser()
    parser.add_option('-f', '--file', action="store", dest="filename")
    parser.add_option('-ner', '--name-entity', default=False) 
    parser.add_option('-i', '--info', default=True )
    opts, args= parser.parser_args()


if __name__ == '__main__':
    main() 
