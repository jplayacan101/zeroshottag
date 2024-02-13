import conllu
import os

import datasets


# _CITATION = """\
# @misc{11234/1-5287,
# title = {Universal Dependencies 2.13},
# author = {Zeman, Daniel and Nivre, Joakim and Abrams, Mitchell and Ackermann, Elia and Aepli, No{\"e}mi and Aghaei, Hamid and Agi{\'c}, {\v Z}eljko and Ahmadi, Amir and Ahrenberg, Lars and Ajede,
# Chika Kennedy and Aleksandravi{\v c}i{\=u}t{\.e}, Gabriel{\.e} and Alfina, Ika and Antonsen, Lene and Aplonova, Katya and Aquino, Angelina and Aragon, Carolina and Aranzabe, Maria Jesus and Ar{\i}can, Bilge Nas and Arnard{\'o}ttir, {\t H}{\'o}runn and Arutie, Gashaw and Arwidarasti, Jessica Naraiswari and Asahara, Masayuki and Aslan, Deniz Baran and Ateyah, Luma and Atmaca, Furkan and Attia, Mohammed and Atutxa, Aitziber and Augustinus, Liesbeth and Badmaeva, Elena and Balasubramani, Keerthana and Ballesteros, Miguel and Banerjee, Esha and Bank, Sebastian and Barbu Mititelu, Verginica and Barkarson, Starkaður and Basmov, Victoria and Batchelor, Colin and Bauer, John and Bedir, Seyyit Talha and Bengoetxea, Kepa and Berk, G{\"o}zde and Berzak, Yevgeni and Bhat, Irshad Ahmad and Bhat, Riyaz Ahmad and Biagetti, Erica and Bick, Eckhard and Bielinskien{\.e}, Agn{\.e} and Bjarnad{\'o}ttir, Krist{\'{\i}}n and Blokland, Rogier and Bobicev, Victoria and Boizou, Lo{\"{\i}}c and Borges V{\"o}lker, Emanuel and B{\"o}rstell, Carl and Bosco, Cristina and Bouma, Gosse and Bowman, Sam and Boyd, Adriane and Braggaar, Anouck and Brokait{\.e}, Kristina and Burchardt, Aljoscha and Candito, Marie and Caron, Bernard and Caron, Gauthier and Cassidy, Lauren and Cavalcanti, Tatiana and Cebiro{\u g}lu Eryi{\u g}it, G{\"u}l{\c s}en and Cecchini, Flavio Massimiliano and Celano, Giuseppe G. A. and {\v C}{\'e}pl{\"o}, Slavom{\'{\i}}r and Cesur, Neslihan and Cetin, Savas and {\c C}etino{\u g}lu, {\"O}zlem and Chalub, Fabricio and Chauhan, Shweta and Chi, Ethan and Chika, Taishi and Cho, Yongseok and Choi, Jinho and Chun, Jayeol and Cignarella, Alessandra T. and Cinkov{\'a}, Silvie and Collomb, Aur{\'e}lie and {\c C}{\"o}ltekin, {\c C}a{\u g}r{\i} and Connor, Miriam and Courtin, Marine and Cristescu, Mihaela and Daniel, Philemon. and Davidson, Elizabeth and de Marneffe, Marie-Catherine and de Paiva, Valeria and Derin, Mehmet Oguz and de Souza, Elvis and Diaz de Ilarraza, Arantza and Dickerson, Carly and Dinakaramani, Arawinda and Di Nuovo, Elisa and Dione, Bamba and Dirix, Peter and Dobrovoljc, Kaja and Dozat, Timothy and Droganova, Kira and Dwivedi, Puneet and Eckhoff, Hanne and Eiche, Sandra and Eli, Marhaba and Elkahky, Ali and Ephrem, Binyam and Erina, Olga and Erjavec, Toma{\v z} and Etienne, Aline and Evelyn, Wograine and Facundes, Sidney and Farkas, Rich{\'a}rd and Fernanda, Mar{\'{\i}}lia and Fernandez Alcalde, Hector and Foster, Jennifer and Freitas, Cl{\'a}udia and Fujita, Kazunori and Gajdo{\v s}ov{\'a}, Katar{\'{\i}}na and Galbraith, Daniel and Garcia, Marcos and G{\"a}rdenfors, Moa and Garza, Sebastian and Gerardi, Fabr{\'{\i}}cio Ferraz and Gerdes, Kim and Ginter, Filip and Godoy, Gustavo and Goenaga, Iakes and Gojenola, Koldo and G{\"o}k{\i}rmak, Memduh and Goldberg, Yoav and G{\'o}mez Guinovart, Xavier and Gonz{\'a}lez Saavedra,
# Berta and Grici{\=u}t{\.e}, Bernadeta and Grioni, Matias and Grobol,
# Lo{\"{\i}}c and Gr{\=
# u}z{\={\i}}tis, Normunds and Guillaume, Bruno and Guillot-Barbance, C{\'e}line and G{\"u}ng{\"o}r, Tunga and Habash, Nizar and Hafsteinsson, Hinrik and Haji{\v c}, Jan and Haji{\v c} jr., Jan and H{\"a}m{\"a}l{\"a}inen, Mika and H{\`a} M{\~y}, Linh and Han, Na-Rae and Hanifmuti, Muhammad Yudistira and Hardwick, Sam and Harris, Kim and Haug, Dag and Heinecke, Johannes and Hellwig, Oliver and Hennig, Felix and Hladk{\'a}, Barbora and Hlav{\'a}{\v c}ov{\'a}, Jaroslava and Hociung, Florinel and Hohle, Petter and Huber, Eva and Hwang, Jena and Ikeda, Takumi and Ingason, Anton Karl and Ion, Radu and Irimia, Elena and Ishola, {\d O}l{\'a}j{\'{\i}}d{\'e} and Ito, Kaoru and Jel{\'{\i}}nek, Tom{\'a}{\v s} and Jha, Apoorva and Johannsen, Anders and J{\'o}nsd{\'o}ttir, Hildur and J{\o}rgensen, Fredrik and Juutinen, Markus and K, Sarveswaran and Ka{\c s}{\i}kara, H{\"u}ner and Kaasen, Andre and Kabaeva, Nadezhda and Kahane, Sylvain and Kanayama, Hiroshi and Kanerva, Jenna and Kara, Neslihan and Katz, Boris and Kayadelen, Tolga and Kenney, Jessica and Kettnerov{\'a}, V{\'a}clava and Kirchner, Jesse and Klementieva, Elena and K{\"o}hn, Arne and K{\"o}ksal, Abdullatif and Kopacewicz, Kamil and Korkiakangas, Timo and Kotsyba, Natalia and Kovalevskait{\.e}, Jolanta and Krek, Simon and Krishnamurthy, Parameswari and Kuyruk{\c c}u, O{\u g}uzhan and Kuzgun, Asl{\i} and Kwak, Sookyoung and Laippala, Veronika and Lam, Lucia and Lambertino, Lorenzo and Lando, Tatiana and Larasati, Septina Dian and Lavrentiev, Alexei and Lee, John and L{\^e} H{\`{\^o}}ng, Phương and Lenci, Alessandro and Lertpradit, Saran and Leung, Herman and Levina, Maria and Li, Cheuk Ying and Li, Josie and Li, Keying and Li, Yuan and Lim, {KyungTae} and Lima Padovani, Bruna and Lind{\'e}n, Krister and Ljube{\v s}i{\'c}, Nikola and Loginova, Olga and Luthfi, Andry and Luukko, Mikko and Lyashevskaya, Olga and Lynn, Teresa and Macketanz, Vivien and Makazhanov, Aibek and Mandl, Michael and Manning, Christopher and Manurung, Ruli and Mar{\c s}an, B{\"u}{\c s}ra and M{\u a}r{\u a}nduc, C{\u a}t{\u a}lina and Mare{\v c}ek, David and Marheinecke, Katrin and Mart{\'{\i}}nez Alonso, H{\'e}ctor and Martins, Andr{\'e} and Ma{\v s}ek, Jan and Matsuda, Hiroshi and Matsumoto, Yuji and Mazzei, Alessandro and {McDonald}, Ryan and {McGuinness}, Sarah and Mendon{\c c}a, Gustavo and Miekka, Niko and Mischenkova, Karina and Misirpashayeva, Margarita and Missil{\"a}, Anna and Mititelu, C{\u a}t{\u a}lin and Mitrofan, Maria and Miyao, Yusuke and Mojiri Foroushani, {AmirHossein} and Moln{\'a}r, Judit and Moloodi, Amirsaeid and Montemagni, Simonetta and More, Amir and Moreno Romero, Laura and Moretti, Giovanni and Mori, Keiko Sophie and Mori, Shinsuke and Morioka, Tomohiko and Moro, Shigeki and Mortensen, Bjartur and Moskalevskyi, Bohdan and Muischnek, Kadri and Munro, Robert and Murawaki, Yugo and M{\"u}{\"u}risep, Kaili and Nainwani, Pinkey and Nakhl{\'e}, Mariam and Navarro Hor{\~n}iacek, Juan Ignacio and Nedoluzhko,
# Anna and Ne{\v s}pore-B{\=e}rzkalne, Gunta and Nevaci, Manuela and Nguy{\~{\^e}}n Th{\d i}, Lương and Nguy{\~{\^e}}n Th{\d i} Minh, Huy{\`{\^e}}n and Nikaido, Yoshihiro and Nikolaev, Vitaly and Nitisaroj, Rattima and Nourian, Alireza and Nurmi, Hanna and Ojala, Stina and Ojha, Atul Kr. and Ol{\'u}{\`o}kun, Ad{\'e}day{\d o}̀ and Omura, Mai and Onwuegbuzia, Emeka and Osenova, Petya and {\"O}stling, Robert and {\O}vrelid, Lilja and {\"O}zate{\c s}, {\c S}aziye Bet{\"u}l and {\"O}z{\c c}elik, Merve and {\"O}zg{\"u}r, Arzucan and {\"O}zt{\"u}rk Ba{\c s}aran, Balk{\i}z and Park, Hyunji Hayley and Partanen, Niko and Pascual, Elena and Passarotti, Marco and Patejuk, Agnieszka and Paulino-Passos, Guilherme and Peljak-{\L}api{\'n}ska, Angelika and Peng, Siyao and Perez, Cenel-Augusto and Perkova, Natalia and Perrier, Guy and Petrov, Slav and Petrova, Daria and Phelan, Jason and Piitulainen, Jussi and Pirinen, Tommi A and Pitler, Emily and Plank, Barbara and Poibeau, Thierry and Ponomareva, Larisa and Popel, Martin and Pretkalni{\c n}a, Lauma and Pr{\'e}vost, Sophie and Prokopidis, Prokopis and Przepi{\'o}rkowski, Adam and Puolakainen, Tiina and Pyysalo, Sampo and Qi, Peng and R{\"a}{\"a}bis, Andriela and Rademaker, Alexandre and Rama, Taraka and Ramasamy, Loganathan and Ramisch, Carlos and Rashel, Fam and Rasooli, Mohammad Sadegh and Ravishankar, Vinit and Real, Livy and Rebeja, Petru and Reddy, Siva and Rehm, Georg and Riabov, Ivan and Rie{\ss}ler, Michael and Rimkut{\.e}, Erika and Rinaldi, Larissa and Rituma, Laura and Rocha, Luisa and R{\"o}gnvaldsson, Eir{\'{\i}}kur and Romanenko, Mykhailo and Rosa, Rudolf and Roșca, Valentin and Rovati, Davide and Rudina, Olga and Rueter, Jack and R{\'u}narsson, Kristj{\'a}n and Sadde, Shoval and Safari, Pegah and Sagot, Beno{\^{\i}}t and Sahala, Aleksi and Saleh, Shadi and Salomoni, Alessio and Samard{\v z}i{\'c}, Tanja and Samson, Stephanie and Sanguinetti, Manuela and San{\i}yar, Ezgi and S{\"a}rg,
# Dage and Saul{\={\i}}te, Baiba and Sawanakunanon, Yanin and Saxena, Shefali and Scannell, Kevin and Scarlata, Salvatore and Schneider, Nathan and Schuster, Sebastian and Schwartz, Lane and Seddah, Djam{\'e} and Seeker, Wolfgang and Seraji, Mojgan and Shen, Mo and Shimada, Atsuko and Shirasu, Hiroyuki and Shishkina, Yana and Shohibussirri, Muh and Sichinava, Dmitry and Siewert, Janine and Sigurðsson, Einar Freyr and Silveira, Aline and Silveira, Natalia and Simi, Maria and Simionescu, Radu and Simk{\'o}, Katalin and {\v S}imkov{\'a}, M{\'a}ria and Simov, Kiril and Skachedubova, Maria and Smith, Aaron and Soares-Bastos, Isabela and Spadine, Carolyn and Sprugnoli, Rachele and Steingr{\'{\i}}msson, Stein{\t h}{\'o}r and Stella, Antonio and Straka, Milan and Strickland, Emmett and Strnadov{\'a}, Jana and Suhr, Alane and Sulestio, Yogi Lesmana and Sulubacak, Umut and Suzuki, Shingo and Sz{\'a}nt{\'o}, Zsolt and Taji, Dima and Takahashi, Yuta and Tamburini, Fabio and Tan, Mary Ann C. and Tanaka, Takaaki and Tella, Samson and Tellier, Isabelle and Testori, Marinella and Thomas, Guillaume and Torga, Liisi and Toska, Marsida and Trosterud, Trond and Trukhina, Anna and Tsarfaty, Reut and T{\"u}rk, Utku and Tyers, Francis and Uematsu, Sumire and Untilov, Roman and Ure{\v s}ov{\'a}, Zde{\v n}ka and Uria, Larraitz and Uszkoreit, Hans and Utka, Andrius and Vajjala, Sowmya and van der Goot, Rob and Vanhove, Martine and van Niekerk, Daniel and van Noord, Gertjan and Varga, Viktor and Villemonte de la Clergerie, Eric and Vincze, Veronika and Vlasova, Natalia and Wakasa, Aya and Wallenberg, Joel C. and Wallin, Lars and Walsh, Abigail and Wang, Jing Xian and Washington, Jonathan North and Wendt, Maximilan and Widmer, Paul and Williams, Seyi and Wir{\'e}n, Mats and Wittern, Christian and Woldemariam, Tsegay and Wong, Tak-sum and Wr{\'o}blewska, Alina and Yako, Mary and Yamashita, Kayo and Yamazaki, Naoki and Yan, Chunxiao and Yasuoka, Koichi and Yavrumyan, Marat M. and Yenice, Arife Bet{\"u}l and Y{\i}ld{\i}z, Olcay Taner and Yu, Zhuoran and {\v Z}abokrtsk{\'y}, Zden{\v e}k and Zahra, Shorouq and Zeldes, Amir and Zhu, Hanzhi and Zhuravleva, Anna and Ziane, Rayan},
# url = {http://hdl.handle.net/11234/1-3687},
# note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal and Applied Linguistics ({{\'U}FAL}), Faculty of Mathematics and Physics, Charles University},
# copyright = {Licence Universal Dependencies v2.13},
# year = {2021} }
# """  # noqa: W605

_DESCRIPTION = """\
Universal Dependencies is a project that seeks to develop cross-linguistically consistent treebank annotation for many languages, with the goal of facilitating multilingual parser development, cross-lingual learning, and parsing research from a language typology perspective. The annotation scheme is based on (universal) Stanford dependencies (de Marneffe et al., 2006, 2008, 2014), Google universal part-of-speech tags (Petrov et al., 2012), and the Interset interlingua for morphosyntactic tagsets (Zeman, 2008).
"""

_URL = "https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-5287/ud-treebanks-v2.13.tgz"

original_directory = os.getcwd()
new_directory = '/Users/jplayacan/.cache/huggingface/datasets/downloads/extracted/8453fbfded7739b8a75b017ff719af23ed073e893f0988874aac9d45a29b54b1/ud-treebanks-v2.13/'
os.chdir(new_directory)

_UD_DATASETS = {}
for dirname in os.listdir():
    if not os.path.isdir(dirname):
        continue
    lang, dataset = dirname.replace("UD_", "").split("-")
    train, dev, test = None, None, None
    for filename in os.listdir(dirname):
        if not filename.endswith(".conllu"):
            continue
        id_, split = filename.replace(".conllu", "").split("-ud-")
        langid, dataid = id_.split("_")
        print(lang, dataset, langid, dataid, split)
        if langid not in _UD_DATASETS:
            _UD_DATASETS[langid] = {}
        if split not in _UD_DATASETS[langid]:
            _UD_DATASETS[langid][split] = []
        _UD_DATASETS[langid][split].append(os.path.join(dirname, filename))

os.chdir(original_directory)

class Udpos213Config(datasets.BuilderConfig):
    """BuilderConfig for Universal dependencies"""
    def __init__(self, **kwargs):
        super(Udpos213Config, self).__init__(**kwargs)

        self.data_url = _URL


class Udpos213(datasets.GeneratorBasedBuilder):
    VERSION = datasets.Version("2.13.1")  # type: ignore
    # BUILDER_CONFIGS = [Udpos213Config(
    #     name=name,
    #     data_url=_URL,
    # ) for name in _UD_DATASETS]
    BUILDER_CONFIG_CLASS = Udpos213Config

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features({
                "idx":
                datasets.Value("string"),
                # "text":
                # datasets.Value("string"),
                "tokens":
                datasets.Sequence(datasets.Value("string")),
                # "lemmas":
                # datasets.Sequence(datasets.Value("string")),
                "labels":
                datasets.Sequence(
                    datasets.features.ClassLabel(names=[
                        "ADJ",
                        "ADP",
                        "ADV",
                        "AUX",
                        "CCONJ",
                        "DET",
                        "INTJ",
                        "NOUN",
                        "NUM",
                        "PART",
                        "PRON",
                        "PROPN",
                        "PUNCT",
                        "SCONJ",
                        "SYM",
                        "VERB",
                        "X",
                    ])),
                # "xpos":
                # datasets.Sequence(datasets.Value("string")),
                # "feats":
                # datasets.Sequence(datasets.Value("string")),
                # "head":
                # datasets.Sequence(datasets.Value("string")),
                # "deprel":
                # datasets.Sequence(datasets.Value("string")),
                # "deps":
                # datasets.Sequence(datasets.Value("string")),
                # "misc":
                # datasets.Sequence(datasets.Value("string")),
            }),
            supervised_keys=None,
            homepage="https://universaldependencies.org/",
            # citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        downloaded_files = dl_manager.download_and_extract(self.config.data_url)
        data_dir = os.path.join(downloaded_files, "ud-treebanks-v2.13")
        splits = []

        if "-" in self.config.name:
            data_paths = {}
            for name in self.config.name.split("-"):
                if "train" in _UD_DATASETS[name]:
                    data_paths["train"] = [*data_paths.get("train", []), *_UD_DATASETS[name]["train"]]
                if "dev" in _UD_DATASETS[name]:
                    data_paths["dev"] = [*data_paths.get("dev", []), *_UD_DATASETS[name]["dev"]]
                if "test" in _UD_DATASETS[name]:
                    data_paths["test"] = [*data_paths.get("test", []), *_UD_DATASETS[name]["test"]]

        else:
            data_paths = _UD_DATASETS[self.config.name]

        if "train" in data_paths:
            splits.append(
                datasets.SplitGenerator(name=str(datasets.Split.TRAIN),
                                        gen_kwargs={"data_dir": data_dir, "filepaths": data_paths["train"]}))

        if "dev" in data_paths:
            splits.append(
                datasets.SplitGenerator(name=str(datasets.Split.VALIDATION),
                                        gen_kwargs={"data_dir": data_dir, "filepaths": data_paths["dev"]}))

        if "test" in data_paths:
            splits.append(
                datasets.SplitGenerator(name=str(datasets.Split.TEST),
                                        gen_kwargs={"data_dir": data_dir, "filepaths": data_paths["test"]}))

        return splits

    def _generate_examples(self, data_dir, filepaths):
        id = 0
        for path in filepaths:
            path = os.path.join(data_dir, path)
            with open(path, "r", encoding="utf-8") as data_file:
                tokenlist = list(conllu.parse_incr(data_file))
                for sent in tokenlist:
                    if "sent_id" in sent.metadata:
                        idx = sent.metadata["sent_id"]
                    else:
                        idx = id

                    tokens = [token["form"] for token in sent]
                    upos = [token["upos"] for token in sent]
                    if "_" in tokens or "_" in upos:
                        continue

                    # if "text" in sent.metadata:
                    #     txt = sent.metadata["text"]
                    # else:
                    #     txt = " ".join(tokens)

                    yield id, {
                        "idx": str(idx),
                        # "text": txt,
                        "tokens": tokens,
                        # "lemmas": [token["lemma"] for token in sent],
                        "labels": upos,
                        # "xpos": [token["xpos"] for token in sent],
                        # "feats": [str(token["feats"]) for token in sent],
                        # "head": [str(token["head"]) for token in sent],
                        # "deprel": [str(token["deprel"]) for token in sent],
                        # "deps": [str(token["deps"]) for token in sent],
                        # "misc": [str(token["misc"]) for token in sent],
                    }
                    id += 1
