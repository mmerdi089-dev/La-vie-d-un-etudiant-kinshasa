import time

def afficher_dialogue(nom, texte):
    """Affiche un dialogue de manière propre avec un petit temps de pause."""
    print(f"[{nom}] : {texte}")
    time.sleep(1)

# =====================================================================
# BOUCLE PRINCIPALE DE REJOUABILITÉ
# =====================================================================
jouer_encore = True

while jouer_encore:
    # 1. RÉINITIALISATION DES STATISTIQUES À CHAQUE NOUVELLE PARTIE
    competences = 0
    stress = 10
    energie = 100
    argent = 0
    dollars = 0  
    commune = ""
    info_visa = False
    acces_cours = False
    diplome_obtenu = False

    # ==========================================
    # 2. CONFIGURATION DU PERSONNAGE
    # ==========================================
    print("\n==================================================")
    print("          LA VIE D'UN ÉTUDIANT : KINSHASA         ")
    print("             Objectif : Les États-Unis            ")
    print("==================================================")

    nom_hero = input("\nComment s'appelle ton personnage ? ")
    if not nom_hero:
        nom_hero = "Merdi"

    print(f"\nDans quelle commune de Kinshasa habite {nom_hero} ?")
    print("1. Ndjili (Loin de l'ISTA, budget serré)")
    print("2. Bandalungwa / Bandal (Ambiance, budget moyen)")
    print("3. Gombe (Proche des centres, plus de moyens)")

    choix_commune = input("Entre le numéro de ta commune (1, 2 ou 3) : ")

    if choix_commune == "1":
        commune = "Ndjili"
        argent = 3500  
    elif choix_commune == "2":
        commune = "Bandal"
        argent = 6000
    else:
        commune = "Gombe"
        argent = 10000

    # ==========================================
    # 3. LE RÉVEIL ET LE DÉPART (CHAPITRE 1)
    # ==========================================
    print("\n" + "="*50)
    print(f"       CHAPITRE 1 : LE GRAND DÉPART DE {commune.upper()}")
    print("="*50 + "\n")

    print(f"Il est 5h30 du matin à {commune}. Une fine pluie commence à tomber sur Kinshasa.")
    afficher_dialogue("Maman", f"{nom_hero} ! Réveille-toi mon fils ! Le déjeuner est prêt, tu vas rater le début des cours à l'ISTA !")
    afficher_dialogue(nom_hero, "Oui maman, je me prépare vite et je prends mon sac...")

    print(f"\nTu sors de la parcelle.")
    print(f"💰 Ton portefeuille contient : {argent} FC.")
    print("Le boulevard est déjà complètement bloqué par les embouteillages.")
    print("Comment vas-tu te rendre à l'école ce matin ?")
    print("1. Prendre un 'Esprit de Vie' (2500 FC) - Abrité mais très lent.")
    print("2. Prendre une moto (4500 FC) - Rapide mais cher et sous la pluie.")

    choix_transport = input("\nFais ton choix (1 ou 2) : ")

    if choix_transport == "1":
        argent -= 2500
        print("\nTu montes dans le bus. C'est l'ambiance des transports de Kin !")
        print("Le trajet est interminable. Tu arrives en retard.")
        energie -= 20
        stress += 15
    elif choix_transport == "2":
        if argent >= 4500:
            argent -= 4500
            print("\nLe motard accélère et slalome sur le boulevard !")
            print("Tu arrives super vite devant l'ISTA.")
            energie -= 5
            stress -= 5
        else:
            print("\n❌ Pas assez d'argent pour la moto ! Tu cours sous la pluie pour attraper le bus.")
            argent -= 2500
            energie -= 30
            stress += 25

    # ==========================================
    # 4. LE PORTAIL DE L'ISTA (CHAPITRE 2)
    # ==========================================
    print("\n" + "="*50)
    print("       CHAPITRE 2 : LE PORTAIL DE L'ISTA")
    print("="*50 + "\n")

    print("Devant la porte de ton auditoire, les assistants bloquent l'entrée :")
    print("⚠️ 'Contrôle serré ! Préparez vos reçus de paiement !'")

    afficher_dialogue("Le Délégué", f"Oi, {nom_hero} ! Tu as ton reçu avec toi ? L'assistant rigole pas aujourd'hui !")

    print("\nQuelle est ta situation actuelle ?")
    print("1. 'Oui, j'ai mes documents en règle.'")
    print("2. 'Ah mince... oublié mon reçu à la maison !'")
    print("3. Tenter de négocier poliment avec l'assistant.")

    choix_controle = input("\nEntre ton choix (1, 2 ou 3) : ")

    if choix_controle == "1":
        print("\nTu sors ton reçu. L'assistant vérifie et te laisse passer.")
        acces_cours = True
        competences += 5  
    elif choix_controle == "2":
        print("\nPanique ! Le reçu est resté sur la table de nuit.")
        if argent >= 2000:
            print(f"💡 [Option] Le Délégué chuchote : 'Achète mon syllabus à 2000 FC, je te fais entrer.'")
            choix_secours = input("Acceptes-tu ? (OUI / NON) : ").upper()
            if choix_secours == "OUI" or choix_secours == "O":
                argent -= 2000
                print("Tu entres en classe grâce au syllabus !")
                acces_cours = True
            else:
                print("Tu restes dehors.")
        else:
            print("Pas assez d'argent pour le syllabus. Tu rates le cours.")
    else:
        print("\nL'assistant reconnaît ton sérieux et te laisse entrer exceptionnellement.")
        acces_cours = True

    if acces_cours:
        competences += 15
    else:
        stress += 20

    # ==========================================
    # 5. LA PAUSE ET LE LABO (CHAPITRE 3)
    # ==========================================
    print("\n" + "="*50)
    print("       CHAPITRE 3 : LA PAUSE ET LE LABO")
    print("="*50 + "\n")

    afficher_dialogue("Jérémie", "Oi ! Viens au labo, on va coder en Python !")
    afficher_dialogue("Sarah", "Attends, viens plutôt planifier les démarches de ton Visa américain !")

    print("\nQue décides-tu ?")
    print("1. Aller au labo informatique (Priorité Compétences)")
    print("2. Rester avec Sarah pour le dossier Visa")
    print("3. Aller manger un morceau (Recharge Énergie)")

    choix_aprem = input("\nEntre ton choix (1, 2 ou 3) : ")

    if choix_aprem == "1":
        print("\n💻 Séance de code intense au labo !")
        if acces_cours:
            print("Grâce au cours du matin, tu maîtrises parfaitement l'exercice !")
            competences += 20
        else:
            print("Sans le cours du matin, tu galères mais tu apprends quand même.")
            competences += 10
        energie -= 15
    elif choix_aprem == "2":
        print("\n📂 Sarah t'explique tout sur le dossier consulaire.")
        info_visa = True
        competences += 5
    else:
        if argent >= 1500:
            argent -= 1500
            print("\n🥖 Un bon pain chargé ! Tu récupères toute ton énergie.")
            energie += 30
        else:
            print("\nPas assez de sous, tu bois juste de l'eau.")
            energie -= 10

    # ==========================================
    # 6. LA SESSION D'EXAMENS : ÉVITER LE DIANKO (CHAPITRE 4)
    # ==========================================
    print("\n" + "="*50)
    print("       CHAPITRE 4 : LA SESSION D'EXAMENS À L'ISTA")
    print("="*50 + "\n")

    print(f"C'est l'examen final. Score requis : 10. Ton score : {competences}")
    print("1. Compter sur ta propre logique.")
    print("2. Tenter de tricher (Risque de ZÉRO).")

    choix_examen = input("\nTon choix (1 ou 2) : ")

    if choix_examen == "1":
        if competences >= 10:
            print("\n🔥 Pas de zéro pour toi ! Tu valides l'année haut la main !")
            diplome_obtenu = True
        else:
            print("\n⚠️ Pas assez de points ! Tu passes de justesse grâce au rattrapage.")
            diplome_obtenu = True
    else:
        print("\n❌ Pris en flagrant délit ! L'assistant te colle un ZÉRO en rouge !")

    # ==========================================
    # 7. LE VERDICT DE L'ANNÉE ACADÉMIQUE
    # ==========================================
    print("\n" + "="*50)
    print("       LE VERDICT DE L'ISTA")
    print("="*50)

    if diplome_obtenu:
        print(f"🎉 Félicitations {nom_hero} ! Tu as bravé la session, évité le zéro et validé ton année !")
        print("Tu obtiens ton diplôme. En route pour les démarches ! ✈️")
        
        input("\nAppuie sur Entrée pour te rendre à ton entretien de Visa...")
        
        print("\n" + "="*50)
        print("       CHAPITRE FINAL : L'AMBASSADE DES ÉTATS-UNIS")
        print("="*50 + "\n")
        print("Tu te présentes devant l'agent consulaire américain.")
        
        if info_visa:
            print("💡 Grâce aux conseils de Sarah, ton dossier est parfaitement préparé !")
            print("L'agent examine tes notes, sourit et tamponne ton passeport : VISA ACCORDÉ ! 🇺🇸")
            
            # ==========================================
            # 8. L'AÉROPORT DE N'DJILI : LE GRAND DÉPART (CHAPITRE 5)
            # ==========================================
            print("\n" + "="*50)
            print("       CHAPITRE 5 : L'AÉROPORT DE N'DJILI")
            print("="*50 + "\n")

            print("Tu arrives à l'aéroport de N'djili avec ton père.")
            afficher_dialogue("Mon Père", "Merdi, mon fils, reste concentré sur tes études d'informatique aux USA. Ne l'oublie jamais.")

            input("\nAppuie sur Entrée pour décoller...")

            # ==========================================
            # 9. ÉPILOGUE : BIENVENUE AUX USA
            # ==========================================
            print("\n" + "="*50)
            print("       ÉPILOGUE : UN NOUVEAU DÉPART ")
            print("="*50 + "\n")
            
            afficher_dialogue("Mon Oncle", f"Welcome to America, {nom_hero} !")
            dollars = 100  

            # ==========================================
            # 10. SAISON 2 - CHAPITRE 6 : LE CHOC DU CAMPUS
            # ==========================================
            print("\n" + "="*50)
            print("       SAISON 2 - CHAPITRE 6 : LE CHOC DU CAMPUS")
            print("="*50 + "\n")
            
            print("C'est l'heure de ton tout premier grand cours d'algorithmique avancée.")
            print("1. Lever la main et répondre.")
            print("2. Rester discret.")
            
            choix_campus = input("\nEntre ton choix (1 ou 2) : ")
            if choix_campus == "1":
                competences += 20
            else:
                competences += 5

            # ==========================================
            # 11. SAISON 2 - CHAPITRE 7 : LE DILEMME AMÉRICAIN
            # ==========================================
            print("\n" + "="*50)
            print("       SAISON 2 - CHAPITRE 7 : LE DILEMME AMÉRICAIN")
            print("="*50 + "\n")
            
            print("1. Prendre le job à la bibliothèque (+40 $)")
            print("2. Coder toute la nuit au labo universitaire")

            choix_temps = input("\nEntre ton choix (1 ou 2) : ")
            if choix_temps == "1":
                dollars += 40
            else:
                competences += 25

            # =====================================================================
            # 12. SAISON 2 - CHAPITRE 8 : LE HACKATHON UNIVERSITAIRE
            # =====================================================================
            print("\n" + "="*50)
            print("       SAISON 2 - CHAPITRE 8 : LE HACKATHON UNIVERSITAIRE")
            print("="*50 + "\n")
            
            print("1. Coder l'algorithme principal")
            print("2. Gérer l'interface (Moins risqué)")

            choix_hackathon = input("\nEntre ton choix (1 ou 2) : ")
            if choix_hackathon == "1" and competences >= 30:
                print("🥇 Victoire au Hackathon ! +500 $")
                dollars += 500
                competences += 15
            else:
                print("🥈 Bon projet d'équipe ! +50 $")
                dollars += 50
                competences += 10

            # =====================================================================
            # 13. SAISON 2 - CHAPITRE 9 : L'APPEL DU PAYS
            # =====================================================================
            print("\n" + "="*50)
            print("       SAISON 2 - CHAPITRE 9 : L'APPEL DU PAYS")
            print("="*50 + "\n")
            
            afficher_dialogue("Mon Père", "Allô Merdi ? Jérémie et tes anciens potes de l'ISTA ont besoin d'aide mpona club de code...")
            
            print(f"\nSolde actuel : {dollars} $.")
            print("1. Envoyer 150 $ à Kinshasa pour leur connexion Internet.")
            print("2. Partager tes cours gratuitement sur GitHub.")
            print("3. Te concentrer sur tes dépenses aux USA pour l'instant.")

            choix_pays = input("\nEntre ton choix (1, 2 ou 3) : ")

            if choix_pays == "1" and dollars >= 150:
                dollars -= 150
                print("\n❤️ Geste magnifique ! L'ISTA te remercie !")
            elif choix_pays == "2":
                print("\n💻 Ton GitHub aide tout Kinshasa !")
                competences += 15
            else:
                print("\n💼 Choix pragmatique pour tes études.")

            # =====================================================================
            # 14. SAISON 2 - CHAPITRE 10 : LE PREMIER STAGE
            # =====================================================================
            print("\n" + "="*50)
            print("       SAISON 2 - CHAPITRE 10 : LE PREMIER STAGE")
            print("="*50 + "\n")
            
            print("La fin de l'année approche aux USA. C'est le moment de postuler pour un stage d'été.")
            afficher_dialogue("Recruteur", "Hi Merdi! Si notre base de données Python plante en pleine production, quelle est ta réaction ?")
            
            print("1. Proposer d'optimiser les requêtes avec un système de cache (Demande au moins 50 compétences).")
            print("2. Analyser calmement les logs d'erreurs pour trouver la ligne qui bloque.")
            print("3. Paniquer et couper discrètement ta connexion Internet.")

            choix_stage = input("\nEntre ton choix (1, 2 ou 3) : ")

            if choix_stage == "1":
                if competences >= 50:
                    print("\n🔥 Réponse d'expert ! Stage décroché à 1200 $ par mois !")
                    dollars += 1200
                    competences += 20
                else:
                    print("\n❌ Trop juste techniquement. Le stage te passe sous le nez.")
            elif choix_stage == "2":
                print("\n👍 Réponse humble et pro ! Tu décroches un stage à 600 $ par mois.")
                dollars += 600
                competences += 15
            else:
                print("\n🤦 Recruteur pas dupe. Blacklisté, tu passes ton été à réviser.")

            # =====================================================================
            # 15. SAISON 3 - CHAPITRE 11 : LE LANCEMENT DU CENTRE (NOUVEAU !)
            # =====================================================================
            print("\n" + "="*50)
            print("       SAISON 3 - CHAPITRE 11 : LE LANCEMENT DU CENTRE")
            print("="*50 + "\n")
            
            print("L'été s'achève. Fort de ton expérience américaine, tu passes au niveau supérieur.")
            print("Tu lances officiellement ton centre de programmation et de technologie à distance pour Kinshasa !")
            print("Jérémie t'appelle sur WhatsApp, surexcité, depuis un petit local trouvé près de l'université.")
            
            afficher_dialogue("Jérémie", f"Merdi mon frère, le local est là ! Mais pour attirer du monde et former efficacement les étudiants, il nous faut une vraie stratégie. On commence comment ?")
            
            print(f"\nSolde actuel : {dollars} $.")
            print("1. Investir gros : Envoyer 500 $ pour équiper le local en ordinateurs reconditionnés (Demande au moins 500 $).")
            print("2. Axer sur le contenu : Lancer des Reels et des vidéos courtes sur Facebook pour créer une communauté de codeurs en ligne.")
            print("3. Ouvrir pas à pas : Commencer par des sessions de mentorat gratuites une fois par semaine sur Zoom.")

            choix_centre = input("\nEntre ton choix (1, 2 ou 3) : ")

            print("\n" + "-"*30)
            print("🚀 L'ENVOL DU CENTRE TECH 🚀")
            print("-"*30)

            if choix_centre == "1":
                if dollars >= 500:
                    dollars -= 500
                    print("\n🖥️ Équipement au top ! Les ordinateurs arrivent à Kinshasa.")
                    print("Le centre ouvre ses portes en physique. C'est le premier Tech Lab de ton réseau !")
                    competences += 25
                else:
                    print(f"\n❌ Tu n'as pas les fonds nécessaires ({dollars} $). Tu te rabats sur la création de vidéos en ligne.")
                    print("Tes Reels commencent à faire le buzz auprès des étudiants de Kinshasa !")
                    competences += 15
            elif choix_centre == "2":
                print("\n📱 Stratégie médias au top ! Tes Reels Facebook explosent les compteurs à Kinshasa.")
                print("Le projet devient viral, tu gagnes le badge 'Créateur en vogue' et la communauté s'agrandit !")
                competences += 20
            else:
                print("\n🤝 Le mentorat à distance crée des liens forts.")
                print("Les étudiants de l'ISTA progressent vite grâce à tes conseils directs chaque week-end.")
                competences += 15

            print("\n" + "="*50)
            print("       🏆 FIN DE LA SESSION : BILAN SAISON 3 🏆")
            print("="*50)
            print(f"Quel parcours depuis ton départ ! Ton centre commence à rayonner.")
            print(f"Stats finales globales -> Compétences Code : {competences} | Solde : {dollars} $")

        else:
            print("❌ L'agent regarde tes papiers... 'Il vous manque le dossier de Sarah.'")
            print("Le visa est refusé.")
    else:
        print(f"😭 DIANKO...")

    print("\n==================== FIN DE LA SESSION ====================")
    reponse = input("\nVeux-tu rejouer ? (OUI / NON) : ").upper()
    if reponse != "OUI" and reponse != "O":
        jouer_encore = False
            # =====================================================================
            # 16. SAISON 3 - CHAPITRE 12 : LE CHOC DU DÉLESTAGE (NOUVEAU !)
            # =====================================================================
            print("\n" + "="*50)
            print("       SAISON 3 - CHAPITRE 12 : LE CHOC DU DÉLESTAGE")
            print("="*50 + "\n")
            
            print("Quelques semaines plus tard, le centre tourne à plein régime.")
            print("Tu es en train de donner un cours magistral sur les API en Python sur Zoom depuis les USA.")
            print("Soudain, l'image de Jérémie se coupe. Plus aucun étudiant de Kinshasa ne répond...")
            print("Quelques minutes après, Jérémie t'envoie un message vocal sur WhatsApp :")
            
            afficher_dialogue("Jérémie", "Merdi, mon frère ! Gros délestage dans le quartier, SNEL a coupé le courant ! Tout le labo est éteint et les batteries des téléphones des étudiants baissent vite...")
            
            print(f"\nSolde actuel : {dollars} $ | Tes compétences : {competences}")
            print("Le cours est interrompu. Que décides-tu de faire ?")
            print("1. Acheter un groupe électrogène en urgence (Coûte 300 $ - Sécurise le centre physiquement).")
            print("2. Passer en mode 'Mobile First' (Gratuit - Tu demandes aux étudiants de suivre le cours sur leur téléphone avec la 4G).")
            print("3. Reporter la session à demain (Gratuit - Tu annules le cours pour aujourd'hui).")

            choix_delestage = input("\nEntre ton choix (1, 2 ou 3) : ")

            print("\n" + "-"*30)
            print("⚡ LE VERDICT DE LA SNEL ⚡")
            print("-"*30)

            if choix_delestage == "1":
                if dollars >= 300:
                    dollars -= 300
                    competences += 15
                    print("\n🔌 Solution radicale ! Tu envoies 300 $ par Mobile Money.")
                    print("Jérémie court acheter un groupe électrogène. 15 minutes après, la lumière revient !")
                    print("Les étudiants de l'ISTA crient de joie. Ton centre gagne une réputation de fer.")
                else:
                    print(f"\n❌ Tu n'as pas les 300 $ nécessaires (Solde : {dollars} $). Tu es obligé de reporter le cours.")
                    competences += 5
            elif choix_delestage == "2":
                print("\n📱 Tu t'adaptes ! Tu coupes ta caméra et tu partages un tableau blanc léger.")
                print("Les étudiants se connectent sur leurs téléphones. C'est difficile mais la session se termine.")
                print("Tu gagnes des points de compétences pour ta flexibilité et ta gestion de crise !")
                competences += 20
            else:
                print("\n💤 Session reportée. Les coupures font partie du quotidien à Kinshasa.")
                print("Les étudiants sont un peu déçus, mais ils comprennent la situation.")
                competences += 5

                    # =====================================================================
            # 17. SAISON 3 - CHAPITRE 13 : LA MONÉTISATION ET LA PUB FACEBOOK
            # =====================================================================
            print("\n" + "="*50)
            print("       SAISON 3 - CHAPITRE 13 : LE BOOST DES RÉSEAUX")
            print("="*50 + "\n")
            
            print("Grâce à tes Reels Facebook réguliers, ta page commence à exploser en RDC.")
            print("Les demandes d'inscription au centre tech affluent de partout, même de Lubumbashi et Goma !")
            print("Jérémie t'envoie un message : 'Merdi, on a une communauté en or. Mais pour grandir, il faut choisir notre modèle.'")
            
            print(f"\nSolde actuel : {dollars} $ | Compétences : {competences}")
            print("Quelle stratégie choisis-tu pour développer l'audience du centre ?")
            print("1. Investir dans la pub Facebook (Coûte 100 $ - Propulse tes Reels pour toucher 50 000 étudiants en RDC).")
            print("2. Rendre les certificats Python payants (Rapporte +200 $, mais seuls les étudiants qui paient auront le diplôme du centre).")
            print("3. Rester 100% gratuit et organique (Gratuit - Tu comptes uniquement sur le partage de la communauté).")

            choix_pub = input("\nEntre ton choix (1, 2 ou 3) : ")

            print("\n" + "-"*30)
            print("📈 LE BILAN AUDIENCE 📈")
            print("-"*30)

            if choix_pub == "1":
                if dollars >= 100:
                    dollars -= 100
                    competences += 25
                    print("\n🔥 L'algorithme Facebook s'affole ! Ton compteur de vues explose.")
                    print("Des vagues de nouveaux étudiants rejoignent le groupe d'apprentissage.")
                    print("Tu gagnes une énorme visibilité en tant que jeune leader tech.")
                else:
                    print(f"\n❌ Pas assez de dollars ({dollars} $) pour la pub. Tu restes sur un partage classique.")
                    competences += 10
            elif choix_pub == "2":
                dollars += 200
                competences += 10
                print("\n💰 Le centre commence à s'autofinancer ! Les premiers dollars congolais tombent.")
                print("Certains étudiants râlent un peu, mais cela donne de la valeur à tes certifications.")
            else:
                print("\n🌱 Progression tranquille et solide. La communauté avance grâce au bouche-à-oreille.")
                print("Les étudiants te respectent énormément pour ton aide totalement gratuite.")
                competences += 15

            print(f"\nStats après ce choix -> Compétences : {competences} | Solde : {dollars} $")
    print(f"\nStats après cette crise -> Compétences : {competences} | Solde : {dollars} $")
            # =====================================================================
            # 18. SAISON 3 - CHAPITRE 14 : LE PREMIER HACKATHON DE KINSHASA
            # =====================================================================
            print("\n" + "="*50)
            print("       SAISON 3 - CHAPITRE 14 : LE HACKATHON DE KINSHASA")
            print("="*50 + "\n")
            
            print("Pour fêter les avancées du centre, tu décides de frapper un grand coup.")
            print("Tu organises le tout premier Hackathon en ligne et en physique pour tes étudiants.")
            print("L'objectif : coder un script Python utile pour la communauté locale en 48 heures chrono.")
            
            afficher_dialogue("Jérémie", "Merdi, l'ambiance est survoltée au labo ! Tout le monde veut participer. Mais pour motiver les troupes, il nous faut un prix légendaire !")
            
            print(f"\nSolde actuel : {dollars} $ | Compétences : {competences}")
            print("Quel prix ou récompense décides-tu d'offrir pour ce Hackathon ?")
            print("1. Offrir un gros cash prize (Coûte 250 $ - Le gagnant repart avec une belle somme pour financer ses projets).")
            print("2. Partenariat d'incubation (Gratuit - Tu contactes une startup locale pour offrir un stage au vainqueur).")
            print("3. Offrir des ressources Cloud et des accès Premium (Coûte 50 $ - Tu offres des abonnements de code pro).")

            choix_hackathon_kin = input("\nEntre ton choix (1, 2 ou 3) : ")

            print("\n" + "-"*30)
            print("🏆 RÉSULTATS DU HACKATHON 🏆")
            print("-"*30)

            if choix_hackathon_kin == "1":
                if dollars >= 250:
                    dollars -= 250
                    competences += 30
                    print("\n💰 Événement historique ! Avec 250 $ en jeu, les étudiants se surpassent.")
                    print("L'équipe gagnante crée un système d'alerte pour les embouteillages de Kinshasa.")
                    print("Ton centre fait la une des discussions tech sur les réseaux en RDC !")
                else:
                    print(f"\n❌ Solde insuffisant ({dollars} $). Tu bascules automatiquement sur l'option Stage local.")
                    competences += 15
            elif choix_hackathon_kin == "2":
                competences += 20
                print("\n💼 Choix hyper pro ! Une startup de la place accepte de prendre le gagnant en stage.")
                print("Les étudiants voient que ton centre ouvre de vraies portes vers l'emploi.")
                print("Jérémie est fier de cette connexion avec le monde professionnel.")
            else:
                if dollars >= 50:
                    dollars -= 50
                    competences += 20
                    print("\n💻 Les codeurs adorent les outils pro ! Les gagnants reçoivent leurs licences.")
                    print("Ils ont désormais tout ce qu'il faut pour pousser leurs projets Python encore plus loin.")
                else:
                    print(f"\n❌ Même 50 $ c'est trop pour ton solde actuel. Le hackathon reste amical, l'ambiance est bonne !")
                    competences += 10

            print(f"\nStats après le Hackathon -> Compétences : {competences} | Solde : {dollars} $")
            # =====================================================================
            # 19. SAISON 3 - CHAPITRE 15 : LA PROPOSITION D'UNE GRANDE BANQUE
            # =====================================================================
            print("\n" + "="*50)
            print("       SAISON 3 - CHAPITRE 15 : L'OFFRE INATTENDUE")
            print("="*50 + "\n")
            
            print("Le succès du Hackathon et de tes Reels Facebook est remonté aux oreilles des grands directeurs.")
            print("Le directeur de l'innovation d'une grande banque basée à Gombe t'envoie un e-mail officiel.")
            print("Ils adorent ce que tu as bâti à distance et te font une proposition sérieuse :")
            print("💡 'Nous voulons racheter votre concept pour en faire notre académie interne, ou financer des bourses.'")
            
            print(f"\nSolde actuel : {dollars} $ | Compétences : {competences}")
            print("C'est un tournant majeur pour l'avenir de ton centre. Quelle est ta décision ?")
            print("1. Accepter le rachat total (Rapporte +2000 $ immédiatement - La banque devient propriétaire, tu perds le contrôle).")
            print("2. Refuser le rachat mais négocier un partenariat de bourses (Demande 100 compétences - Tu restes le boss, ils financent tes étudiants).")
            print("3. Refuser catégoriquement (Gratuit - Tu restes 100% indépendant et autonome).")

            choix_banque = input("\nEntre ton choix (1, 2 ou 3) : ")

            print("\n" + "-"*30)
            print("💼 LA STRATÉGIE CORPORATE 💼")
            print("-"*30)

            if choix_banque == "1":
                dollars += 2000
                print("\n💰 Le compte bancaire explose ! Tu reçois 2000 $ sur ton solde américain.")
                print("Le centre change de nom et arbore le logo de la banque. Tu es riche, mais le projet ne t'appartient plus.")
                print("Jérémie devient un salarié de la banque à Kinshasa.")
            elif choix_banque == "2":
                if competences >= 100:
                    dollars += 500
                    competences += 30
                    print("\n🔥 Négociation de haut niveau ! Ton profil de codeur-entrepreneur a impressionné la banque.")
                    print("Tu gardes le contrôle total du centre. En plus, la banque finance 500 $ de bourses pour tes meilleurs étudiants.")
                    print("C'est le scénario parfait : indépendance et moyens financiers !")
                else:
                    print(f"\n❌ Tes compétences actuelles ({competences}) sont trop justes pour imposer tes conditions.")
                    print("La banque retire son offre. Tu restes indépendant mais sans leur financement.")
                    competences += 10
            else:
                competences += 20
                print("\n✊ 'L'indépendance n'a pas de prix !' Tu refuses poliment leur argent.")
                print("La communauté internet te salue pour ton intégrité. Tu restes le seul maître à bord.")
                print("Jérémie te valide à 100% : 'C'est ça la vision, mon frère !'")

            print(f"\nStats après les négociations -> Compétences : {competences} | Solde : {dollars} $")
            # =====================================================================
            # 20. SAISON 3 - CHAPITRE 16 : L'ÉPILOGUE ET LE CHOIX DU DESTIN
            # =====================================================================
            print("\n" + "="*50)
            print("       SAISON 3 - CHAPITRE 16 : LE CHOIX DU DESTIN")
            print("="*50 + "\n")
            
            print("L'année académique et tes projets aux USA touchent à leur fin.")
            print("Grâce à ton travail acharné, ton diplôme en informatique est validé.")
            print("À Kinshasa, le centre de programmation est devenu une véritable institution de référence.")
            print("Ton père t'appelle pour faire un bilan de la situation et parler de l'avenir.")
            
            afficher_dialogue("Mon Père", "Mon fils, je suis tellement fier de ce que tu as accompli à distance. Les étudiants de l'ISTA et de tout Kinshasa parlent de toi. Maintenant que tu as ton diplôme américain, quelle est la suite ?")
            
            print(f"\n--- BILAN FINAL DE TON PARCOURS ---")
            print(f"🧠 Compétences acquises : {competences}")
            print(f"💰 Capital financier : {dollars} $")
            print(f"-----------------------------------")
            
            print("\nQuel destin choisis-tu pour sceller la fin de la Saison 3 ?")
            print("1. Le Grand Retour (Rentrer physiquement à Kinshasa pour inaugurer un immense Tech Hub en personne).")
            print("2. L'Ingénieur Global (Rester bosser aux USA dans une grande entreprise tout en gérant le centre à distance avec Jérémie).")

            choix_destin = input("\nEntre ton choix (1 ou 2) : ")

            print("\n" + "="*50)
            print("       🎉 LE MOT DE LA FIN 🎉")
            print("="*50)

            if choix_destin == "1":
                print(f"\n✈️ Tu boucles tes valises et tu prends le vol retour vers l'aéroport de N'djili !")
                print("À ton arrivée, Jérémie, ton père et des dizaines d'étudiants t'attendent avec des applaudissements.")
                print("Tu coupes le ruban symbolique de ton nouveau centre de codage physique.")
                print(f"Félicitations {nom_hero}, tu es revenu investir chez toi pour former la prochaine génération de génies tech en RDC ! 🇨🇩")
            else:
                print(f"\n🇺🇸 Tu signes ton premier contrat de travail dans une grande entreprise de la Silicon Valley.")
                print("Tu restes basé aux USA, mais tu n'oublies pas tes racines.")
                print("Chaque mois, tu finances le labo et tu passes des heures sur Zoom pour guider les codeurs de Kinshasa.")
                print(f"Félicitations {nom_hero}, tu es devenu un pont solide entre la tech américaine et la jeunesse congolaise ! 🌐")

            print("\n" + "="*50)
            print("       🏆 FIN DE LA SAISON 3 : JEU TERMINÉ 🏆")
            print("="*50)
            print(f"Score final global -> Compétences : {competences} | Solde : {dollars} $")
