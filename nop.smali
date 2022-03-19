.class public Lcom/example/helloworldlab/MainActivity;
.super Landroidx/appcompat/app/AppCompatActivity;
.source "MainActivity.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .line 7
    invoke-direct {p0}, Landroidx/appcompat/app/AppCompatActivity;-><init>()V

    return-void
	nop
	nop
	nop
	nop
.end method


# virtual methods
.method public fun(I)I
    .locals 5

    const/4 v0, 0x0
	nop
	nop

    const/4 v1, 0x0
	nop
	nop
	nop
	nop

    const/4 v2, 0x0
	nop
	nop
	nop

    :goto_0
    if-ge v1, p1, :cond_1
	nop
	nop
	nop
	nop
	nop

    const/4 v3, 0x0
	nop
	nop

    :goto_1
    if-ge v3, p1, :cond_0
	nop
	nop

    add-int/2addr v2, v3
	nop
	nop
	nop
	nop

    const-string v4, "HELLO"
	nop

    .line 24
    invoke-static {v4, v4}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I

    add-int/lit8 v3, v3, 0x1
	nop
	nop
	nop
	nop
	nop

    goto :goto_1
	nop
	nop

    :cond_0
    add-int/lit8 v1, v1, 0x1
	nop

    goto :goto_0
	nop
	nop

    :cond_1
    return v2
	nop
	nop
.end method

.method protected onCreate(Landroid/os/Bundle;)V
    .locals 3

    const/16 v0, 0xa
	nop
	nop
	nop
	nop
	nop

    .line 11
    invoke-virtual {p0, v0}, Lcom/example/helloworldlab/MainActivity;->fun(I)I

    move-result v0
	nop
	nop

    .line 12
    new-instance v1, Ljava/lang/StringBuilder;
	nop
	nop
	nop
	nop
	nop

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "value: "
	nop
	nop

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0
	nop
	nop

    const-string v1, "MYINT"
	nop
	nop
	nop

    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 13
    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    const p1, 0x7f0b001c
	nop

    .line 14
    invoke-virtual {p0, p1}, Lcom/example/helloworldlab/MainActivity;->setContentView(I)V

    return-void
	nop
.end method
