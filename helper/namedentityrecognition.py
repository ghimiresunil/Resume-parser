import nltk
from formatter.formatdata import formatEducationalinfo,formatExperienceinfo,cleandata



class StanfordNER:

    ###----<NER model that chooses the particular model and parser>----###
    @staticmethod
    def ner_parser(model,text,mode):
        words = nltk.word_tokenize(text)
        parser = {
                'profile':StanfordNER.personal_info_parser,
                'academics':StanfordNER.education_parser,
                'experience':StanfordNER.experience_parser,
                }

        tagged_tuples = model.tag(words)
        return parser[mode](tagged_tuples,text)

    @staticmethod
    def experience_parser(tagged_tuples,text):
        o_counter = 0
        alldesignation = []
        alllocations = []
        alldate = []
        allroles =[]
        allcompany= []
        desig_container = []
        loc_container = []
        date_container = []
        roles_container = []
        company_container = []
        for word,tag in tagged_tuples:
            if tag == 'DESIG':
                desig_container.append(word)
            else:
                if desig_container:
                    designation = ' '.join(desig_container)
                    alldesignation.append(designation)
                    desig_container = []
            if tag == 'LOC':
                loc_container.append(word)

            else:
                if loc_container:
                    location = ' '.join(loc_container)
                    loc_container = []
                    alllocations.append(location)
            if tag == 'DATE':
                date_container.append(word)

            else:
                if date_container:
                    date = ' '.join(date_container)
                    alldate.append(date)
                    date_container = []

            if tag == 'O':
                o_counter += 1
                roles_container.append(word)
            else:
                if o_counter > 10:
                    role = ' '.join(roles_container)
                    roles_container = []
                    o_counter = 0
                    allroles.append(role)

            if tag == 'ORG':
                company_container.append(word)
            else:
                if company_container:
                    company = ' '.join(company_container)
                    company_container = []
                    allcompany.append(company)
        if loc_container:
            alllocations.append(' '.join(loc_container))

        if date_container:
            alldate.append(' '.join(date_container))

        if company_container:
            allcompany.append(' '.join(company_container))

        if desig_container:
            alldesignation.append(' '.join(desig_container))
        if roles_container:
            allroles.append(' '.join(roles_container))
        sent_tokens = text.split('\n')
        sent2indx = {}
        item_tracker = {}
        for index,sentence in enumerate(sent_tokens):
            cleaned_sentence = cleandata(sentence)
            if cleaned_sentence not in sent2indx:
                sent2indx.update({cleaned_sentence:index})
                item_tracker.update({cleaned_sentence:1})

            else:

                sent2indx.update({cleaned_sentence+'{}'.format(item_tracker[cleaned_sentence]):index})
                item_tracker[cleaned_sentence] += 1



        experiences = formatExperienceinfo(sent_tokens,sent2indx,alldesignation,
                                          allcompany,alldate,alllocations,allroles)
        return experiences



    @staticmethod
    def education_parser(tagged_tuples,text):
        alldegree = []
        alllocations = []
        alldate = []
        alluniversity = []
        deg_container = []
        loc_container = []
        date_container = []
        university_container = []
        for word,tag in tagged_tuples:
            if tag == 'DEG':
                deg_container.append(word)
            else:
                if deg_container:
                    degree = ' '.join(deg_container)
                    alldegree.append(degree)
                    deg_container = []
            if tag == 'LOC':
                loc_container.append(word)
            else:
                if loc_container:
                    location = ' '.join(loc_container)
                    loc_container = []
                    alllocations.append(location)
            if tag == 'DATE':
                date_container.append(word)
            else:
                if date_container:
                    date = ' '.join(date_container)
                    alldate.append(date)
                    date_container = []
            if tag == 'UNI':
                university_container.append(word)
            else:
                if university_container:
                    university = ' '.join(university_container)
                    university_container = []
                    alluniversity.append(university)

        if loc_container:
            alllocations.append(' '.join(loc_container))

        if date_container:
            alldate.append(' '.join(date_container))

        if university_container:
            alluniversity.append(' '.join(university_container))

        if deg_container:
            alldegree.append(' '.join(deg_container))

        sent_tokens = text.split('\n')
        sent2indx = {}
        item_tracker = {}
        for index, sentence in enumerate(sent_tokens):
            cleaned_sentence = cleandata(sentence)
            if cleaned_sentence not in sent2indx:
                sent2indx.update({cleaned_sentence: index})
                item_tracker.update({cleaned_sentence: 1})

            else:

                sent2indx.update({cleaned_sentence + '{}'.format(item_tracker[cleaned_sentence]): index})
                item_tracker[cleaned_sentence] += 1
        academics = formatEducationalinfo(
                                          sent_tokens, sent2indx, alldegree,
                                          alluniversity, alldate, alllocations
                                          )


        return academics




    @staticmethod
    def personal_info_parser(tagged_tuples,text):
        name = 'Anonymous'
        address = []
        possible_name = []
        possible_address = []

        for word, tag in tagged_tuples:
            if tag == "PER":
                possible_name.append(word)
            else:
                if possible_name:
                    name = (" ".join(possible_name)).lower()
                    possible_name = []

            if tag == "LOC":
                possible_address.append(word)
            else:
                if possible_address:
                    address.append(" ".join(possible_address))
                    possible_address = []
        final_address = list(set(address))
        formatted_name = name.title()
        return formatted_name, final_address




