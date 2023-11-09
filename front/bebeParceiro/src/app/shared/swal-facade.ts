import Swal from 'sweetalert2';


export class SwalFacade {

  /**
   * @description Representa um SweetAlert para informação de erro
   * 
   * @param titulo Obrigatório informar um titulo para o popup
   * @param texto Opcional, um texto extra de ajuda
   * 
   */
  static erro(titulo: string, texto?: string): Promise<any> {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top',
      showConfirmButton: false,
      timer: 2500,
      background: '#DD0707',
      color: '#ffffff',
      iconColor: '#ffffff',
      timerProgressBar: true,
      didOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
      }
    })

    return Toast.fire({
      icon: 'error',
      title: titulo,
      text: texto,
      confirmButtonColor: '#FFA516',
      confirmButtonText: 'Ok'
    })
  }

  /**
   * @description Representa um SweetAlert para informação de sucesso
   * 
   * @param titulo Obrigatório informar um titulo para o popup
   * @param texto Opcional, um texto extra de ajuda
   * 
   */
  static sucesso(titulo: string, texto?: string): Promise<any> {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top',
      showConfirmButton: false,
      timer: 1000,
      background: '#00ac00',
      color: '#ffffff',
      iconColor: '#ffffff',
      timerProgressBar: true,
      didOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
      }
    })

    return Toast.fire({
      icon: 'success',
      title: titulo,
      text: texto
    })
  }

  /**
   * @description Representa um SweetAlert para informação de alerta
   * 
   * @param titulo Obrigatório informar um titulo para o popup
   * @param texto Opcional, um texto extra de ajuda
   * 
   */
  static alerta(titulo: string, texto?: string): Promise<any> {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top',
      showConfirmButton: false,
      timer: 2500,
      background: '#FF5F1F',
      color: '#ffffff',
      iconColor: '#ffffff',
      timerProgressBar: true,
      didOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
      }
    })

    return Toast.fire({
      icon: 'warning',
      title: titulo,
      text: texto
    })
  }

  /**
   * @description Representa um SweetAlert para exclusão de objetos
   * 
   * @param titulo Obrigatório informar um titulo para o popup
   * @param texto Opcional, um texto extra de ajuda
   * 
   */
  static excluir(button: string,titulo: string, texto?: string): Promise<any> {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top',
      showConfirmButton: true,
      confirmButtonText: button,
      confirmButtonColor: '#DD0707',
      showCancelButton: true,
      cancelButtonColor: '#5e5e5e',
      cancelButtonText: 'Cancelar',
      background: '#ffffff',
      color: '#000000',
      iconColor: '#DD0707',
      timerProgressBar: true,
      didOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
      }
    })

    return Toast.fire({
      icon: 'warning',
      title: titulo,
      text: texto,
    })
  }
}