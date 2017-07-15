import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        # 'https://www.maxwell.vrac.puc-rio.br/UsuarioFuncaoInst.php?strSecao=busca',
        # 'https://www.maxwell.vrac.puc-rio.br/UsuarioFuncaoInst.php?strSecao=busca&strNome=&nrTipBus=2&nrPag=1034&nrOrd=1&nrDir=0>',
        # 'https://www.maxwell.vrac.puc-rio.br/UsuarioFuncaoInst.php?strSecao=busca&strNome=&nrTipBus=2&nrPag=1093&nrOrd=1&nrDir=0%3E>',
        'https://www.maxwell.vrac.puc-rio.br/UsuarioFuncaoInst.php?strSecao=busca&strNome=&nrTipBus=2&nrPag=1&nrOrd=1&nrDir=0%3E%3E>',
    ]

    def parse(self, response):

        for tr in response.css('tr.oddNormal'):
            itens = [item.strip() for item in tr.css('td.txtbasetabNormal::text').extract()]

            yield {
                'nome': itens[3],
                'instituicao': itens[4],
                'sistema': itens[5],
                'matricula': itens[6],
            }

        # links = response.css('a.linkNormal')
        # next_page = [l.css('::attr(href)').extract_first() for l in links if "x" in l.css('::text').extract_first()]

        # if next_page is not None and len(next_page) > 0:
        #     next_page = response.urljoin(next_page[0])
        #     yield scrapy.Request(next_page, callback=self.parse)