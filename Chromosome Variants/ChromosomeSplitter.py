class ChromosomeSplitter:
    def __init__(self,input_VcfFile):
        self.input_VcfFile = input_VcfFile

    def split_by_chromosome(self,chromosome_variants = {}) :
        with open(self.input_VcfFile, 'r') as input_vcf:
            for line in input_vcf:
                if line.startswith('#'):
                    continue

                chromosome = line.split('\t')[0]
                if chromosome not in chromosome_variants:
                    file_name = f'{chromosome}.vcf'
                    chromosome_variants[chromosome] = open(file_name, 'w')

                chromosome_variants[chromosome].write(line)

        for chromosome_variant in chromosome_variants.values():
            chromosome_variant.close()

        print('Dosyalar başarılı bir şekilde bölündü.')
 