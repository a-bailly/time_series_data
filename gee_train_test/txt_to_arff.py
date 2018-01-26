import glob
import numpy
import os.path

__author__ = 'ade.bailly@gmail.com'

if __name__ == '__main__':
    _list = glob.glob('./*/*.txt')
    for _file in _list:
        print _file
        new_file = _file[:-4] + '.arff'
        if True: #not os.path.isfile(new_file):
            # Get Dataset Name
            
            name = _file.split('/',2)[1]
            x = numpy.loadtxt(_file)
            labels, x = map(int,x[:,0]), x[:,1:]
            list_labels = set(labels)
            
            with open(new_file, 'w') as of:
                of.write('@relation '+name+'\n\n')
                for i in range(x.shape[1]):
                    of.write('@attribute att'+str(i)+' numeric\n')
                of.write('@attribute target {' + ','.join(map(str,list_labels))+'}\n\n')
                of.write('@data\n')
                for line, c in zip(x,labels):
                    of.write(','.join(map(str,line))+','+str(c)+'\n')
