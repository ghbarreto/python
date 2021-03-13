import user
import admin
import priv

name = user.User("Gabriel", "Barreto")
name.show()

name2 = admin.Admin("Gabriel", "Barreto")
name2.showAd()

priv = priv.Privileges("Ban")
priv.showPriv()


