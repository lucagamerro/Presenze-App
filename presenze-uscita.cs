using System.Windows.Forms;
using System.Drawing;
using System;

public class Gui {
  // Definizione degli oggetti
  static Form f;
  static Label l = new Label();
  static RadioButton r1 = new RadioButton();
  static RadioButton r2 = new RadioButton();
  static Button b1 = new Button();
  static Button b2 = new Button();
  static TextBox name = new TextBox();
  static TextBox sq = new TextBox();
  static TextBox why = new TextBox();
  static string pv = "; ";
  static string capo = "\n";
  static string sn;
  static string motiv;

  // Eventi
  public static void Si (object sender, EventArgs ea) {
    sn = "Verra' all'uscita";
  }

  public static void No (object sender, EventArgs ea) {
    sn = "Non verra' all'uscita";
    f.Controls.Add(why);
  }

  public static void Esci (object sender, EventArgs ea) {
    f.Close();
  }

  public static void Salva (object sender, EventArgs ea) {
    string nome;
    string squad;
    string testo;
    string inizio;
    bool a = false;
    if (why.Text != "Scrivi qui le tue motivazioni") {
      motiv = why.Text;
    }
    nome = name.Text;
    squad = sq.Text;
    inizio = "NOME" + pv + "SQUADRIGLIA" + pv + "PRESENZA" + pv + "MOTIVAZIONE (se assente)" + capo;
    if (System.IO.File.Exists("presenze.csv") == a) {
      testo = inizio + capo + nome + pv + squad + pv + sn + pv + motiv;
    }
    else {
      testo = capo + nome + pv + squad + pv + sn + pv + motiv;
    }
    System.IO.File.AppendAllText("presenze.csv", testo);
    MessageBox.Show("File salvato come presenze.csv nella cartella corrente", "FILE SALVATO!", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
    f.Close();
  }


  // GUI in generale
  public static void Control () {
    l.Font = new System.Drawing.Font("Microsoft Sans Serif", 12.5F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
    l.Size = new System.Drawing.Size(480, 24);
    l.Location = new System.Drawing.Point(10, 10);
    l.Name = "Uscite mansile";
    l.Text = "Uscita mesile";
    r1.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
    r1.Location = new System.Drawing.Point(10, 30);
    r1.TabIndex = 0;
    r1.Click += new EventHandler (Si);
    r1.Name = "r1";
    r1.Text = "Verrò all'uscita";
    r2.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
    r2.Location = new System.Drawing.Point(10, 50);
    r2.TabIndex = 0;
    r2.Click += new EventHandler (No);
    r2.Name = "r1";
    r2.Text = "Non verrò all'uscita";
    b1.Font  = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
    b1.Size = new System.Drawing.Size(480, 24);
    b1.Location = new System.Drawing.Point(250, 510);
    b1.TabIndex = 0;
    b1.Click += new EventHandler (Esci);
    b1.Name = "b1";
    b1.Text = "Esci";
    b2.Font  = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
    b2.Size = new System.Drawing.Size(480, 24);
    b2.Location = new System.Drawing.Point(250, 480);
    b2.TabIndex = 0;
    b2.Click += new EventHandler (Salva);
    b2.Name = "b2";
    b2.Text = "Salva";
    name.Location = new System.Drawing.Point(10, 80);
    name.Name = "name";
    name.Size = new System.Drawing.Size(200, 20);
    name.TabIndex = 0;
    name.Text = "Nome";
    sq.Location = new System.Drawing.Point(10, 110);
    sq.Name = "sq";
    sq.Size = new System.Drawing.Size(200, 20);
    sq.TabIndex = 0;
    sq.Text = "Squadriglia";
    why.Location = new System.Drawing.Point(10, 300);
    why.Name = "why";
    why.Size = new System.Drawing.Size(200, 20);
    why.TabIndex = 0;
    why.Text = "Scrivi qui le tue motivazioni";

  }

  // Run
  public static void Main () {
    f = new Form ();
    f.ControlBox = true;
    f.MaximizeBox = true;
    f.MinimizeBox = true;
    f.Width = 1000;
    f.Height = 580;
    f.Name = "Prova";
    f.Text = "Presenze";
    Console.WriteLine("Premere invio per aprire il Form...");
    Console.ReadLine();
    Control();
    f.Controls.Add(l);
    f.Controls.Add(r1);
    f.Controls.Add(r2);
    f.Controls.Add(b1);
    f.Controls.Add(b2);
    f.Controls.Add(name);
    f.Controls.Add(sq);
    Application.Run (f);
  }
}
