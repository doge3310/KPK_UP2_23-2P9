from peewee import SqliteDatabase, Model, AutoField, CharField, IntegerField, BooleanField, ForeignKeyField


db = SqliteDatabase("database.db")


class Table(Model):
    id = AutoField()

    class Meta:
        database = db


class Room(Table):
    name = IntegerField()
    status = BooleanField()


class Equipment(Table):
    name = CharField()
    status = BooleanField()


class RoomEquipment(Table):
    room_id = ForeignKeyField(Room)
    equipment_id = ForeignKeyField(Equipment)


def main():
    room_1, _ = Room.get_or_create(
        name="412",
        status=True
    )

    equipment_1, _ = Equipment.get_or_create(
        name="computer 412-03",
        status=True
    )

    equipment_2, _ = Equipment.get_or_create(
        name="computer 412-02",
        status=False
    )

    room_trans_1 = RoomEquipment.get_or_create(
        room_id=1,
        equipment_id=1
    )
    
    room_trans_2 = RoomEquipment.get_or_create(
        room_id=1,
        equipment_id=2
    )


if __name__ == "__main__":
    db.create_tables([
        Room,
        Equipment,
        RoomEquipment
    ])

    main()
